#Database Config
db_user = "root"
mysql_db = "angelai"
db_host = "localhost"
db_password = ""
db_port = 3306
query = "SELECT InjectionId, InjectionName, InjectionDescription FROM tablepromptinjection"
query2 = "SELECT SanitizeId, SanitizeName FROM tablesanitize"

#Pinecone Setup
pinecone_api_key = "pcsk_6UrqME_77Zb6THd4igPEaH92Yn7LRcSf65DoTtZz8gm9MSaWGwq6J4gRyvg6rjn4dSL735"
pinecone_region = "us-west1-gcp"
pinecone_db = "angelai"
pinecone_dimension = 384
pinecone_index_name = "angelai"
pinecone_index_host = "https://angelai-bbnnx1q.svc.aped-4627-b74a.pinecone.io"

#Gemini AI Setup
geminiai_api = "AIzaSyAw7PcCbdWQ61j8GsOfI0wq-bQD-irK0cQ"

#Text Classifier Setup
model_name = "protectai/deberta-v3-base-prompt-injection-v2"