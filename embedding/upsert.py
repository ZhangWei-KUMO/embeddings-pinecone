from settings import get_embedding,index

embeds = get_embedding("简短的文本")
meta = {
    "genre":"news",
    "years":2023
}

index.upsert(vectors=[
   ("id_2",embeds,meta)
],namespace="events")