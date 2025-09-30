from PIL import Image
from io import BytesIO
from langchain_core.runnables.graph import MermaidDrawMethod

def show_graph(runnable):
    graph_image = runnable.get_graph().draw_mermaid_png(
        draw_method=MermaidDrawMethod.API,  # Always online API
        output_file_path="../graph.png"
    )
    img = Image.open(BytesIO(graph_image))
    img.show()



