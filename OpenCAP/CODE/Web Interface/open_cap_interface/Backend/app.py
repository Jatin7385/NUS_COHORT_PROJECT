from flask import Flask, render_template
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64

app = Flask(__name__)

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 1, 2, 1]

# Function to generate a Matplotlib plot
def generate_plot():
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Line 1')
    ax.plot(x, y2, label='Line 2')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.legend()
    return fig

# Route to display the page with graphs
@app.route('/')
def index():
    # Generate multiple plots
    plot1 = generate_plot()
    plot2 = generate_plot()

    # Convert plots to images
    canvas1 = FigureCanvas(plot1)
    canvas2 = FigureCanvas(plot2)

    img1 = BytesIO()
    canvas1.print_png(img1)
    img1_data = base64.b64encode(img1.getvalue()).decode('utf-8')

    img2 = BytesIO()
    canvas2.print_png(img2)
    img2_data = base64.b64encode(img2.getvalue()).decode('utf-8')

    return render_template('index.html', img1_data=img1_data, img2_data=img2_data)

if __name__ == '__main__':
    app.run(debug=True)