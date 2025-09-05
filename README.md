Un progetto Python che trasforma una cartella di CV in un database ricercabile semanticamente, usando RAG (Retrieval-Augmented Generation) e embeddings OpenAI. Perfetto per trovare rapidamente candidati con competenze specifiche, la logica si trova nel file main.py e nel file requirements.txt sono inserite le librerie che sono state usate.

Funzionalità:
-Lettura automatica di CV in .txt da una cartella dedicata.

-Suddivisione dei CV in chunk per una migliore gestione delle informazioni.

-Generazione di embeddings tramite OpenAI (text-embedding-3-small).

-Creazione di un database semantico locale con ChromaDB.

-Ricerca intelligente: inserisci una query in linguaggio naturale e trova i CV più rilevanti.
