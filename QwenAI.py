from gradio_client import Client

client = Client("Qwen/Qwen2-72B-Instruct")
result = client.predict(
		query="write 12 points on pros of being enterpreneur",
		history=[],
		system="You are a helpful assistant.",
		api_name="/model_chat"
)
# Extract the response from the result
response = result[1][0][1]
print(response)



