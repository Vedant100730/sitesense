import voyageai
from config import settings
from typing import List

_voyage_client = None

def get_voyage_client():
    global _voyage_client
    # Always re-check the key in case the global was lost in a background task
    if _voyage_client is None:
        api_key = settings.VOYAGE_API_KEY
        if api_key:
            _voyage_client = voyageai.AsyncClient(api_key=api_key)
    return _voyage_client

async def get_embedding(text: str) -> list[float]:
    """
    Get embedding for a single text string.
    Used for query embedding at search time.
    """
    return (await get_embeddings_batch([text]))[0]

async def get_embeddings_batch(
    texts: list[str],
    input_type: str = "document"
) -> list[list[float]]:
    """
    Get embeddings for multiple texts.
    input_type: "document" for ingestion,
                "query" for search queries
    """
    if not texts:
        return []
    
    # Primary: Voyage AI — always try to create client fresh if needed
    api_key = settings.VOYAGE_API_KEY
    if api_key:
        try:
            client = voyageai.AsyncClient(api_key=api_key)
            all_embeddings = []
            batch_size = 32
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                result = await client.embed(
                    batch,
                    model=settings.DEFAULT_EMBED_MODEL or "voyage-3",
                    input_type=input_type
                )
                all_embeddings.extend(result.embeddings)
            return all_embeddings
        except Exception as e:
            print(f"Voyage AI embedding failed: {e}")
            # Fall through to OpenAI fallback
    
    # Fallback: OpenAI
    if settings.OPENAI_API_KEY:
        try:
            from openai import AsyncOpenAI
            oai = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            all_embeddings = []
            # Batch size for OpenAI embeddings is larger, but we'll do one by one or small batches
            # Let's use simple loop as requested or per OpenAI best practice
            for text in texts:
                response = await oai.embeddings.create(
                    input=text,
                    model="text-embedding-3-small"
                )
                all_embeddings.append(response.data[0].embedding)
            return all_embeddings
        except Exception as e:
            print(f"OpenAI embedding failed: {e}")
    
    raise RuntimeError(
        "No embedding provider available. "
        "Set VOYAGE_API_KEY or OPENAI_API_KEY in .env"
    )

async def get_query_embedding(query: str) -> list[float]:
    """Special method for query embedding (different input_type)"""
    result = await get_embeddings_batch([query], input_type="query")
    return result[0]
