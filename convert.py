from flask import Flask, render_template, request, make_response
from PIL import Image
import io


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jpgtopng', methods=['GET'])
def jpgtopng():
    return render_template('jpgtopng.html')

@app.route('/pngtojpg', methods=['GET'])
def pngtojpg():
    return render_template('pngtojpg.html')

@app.route('/webptopng', methods=['GET'])
def webptopng():
    return render_template('webptopng.html')

@app.route('/pngtowebp', methods=['GET'])
def pngtowebp():
    return render_template('pngtowebp.html')

@app.route('/bmptopng', methods=['GET'])
def bmptopng():
    return render_template('bmptopng.html')

@app.route('/pngtobmp', methods=['GET'])
def pngtobmp():
    return render_template('pngtobmp.html')

@app.route('/pngtogif', methods=['GET'])
def pngtogif():
    return render_template('pngtogif.html')

@app.route('/giftopng', methods=['GET'])
def giftopng():
    return render_template('giftopng.html')

@app.route('/pngtopdf', methods=['GET'])
def pngtopdf():
    return render_template('pngtopdf.html')


# /api routes implementation

# jpgtopng converter
@app.route('/api/jpgtopng', methods=['POST'])
def convert_jpg_to_png():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.jpg') and not image_file.filename.endswith('.jpeg'):
        return 'Only JPG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to PNG
    png_image = io.BytesIO()
    image.save(png_image, format='PNG')
    png_image.seek(0)
    
    # create response object with PNG image as attachment
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    
    return response


# pngtojpg converter 
@app.route('/api/pngtojpg', methods=['POST'])
def convert_png_to_jpg():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.png'):
        return 'Only PNG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to JPG
    jpg_image = io.BytesIO()
    image.convert('RGB').save(jpg_image, format='JPEG', quality=85)
    jpg_image.seek(0)
    
    # create response object with JPG image as attachment
    response = make_response(jpg_image.getvalue())
    response.headers.set('Content-Type', 'image/jpeg')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.jpg')
    
    return response

#webptopng converter
@app.route('/api/webptopng', methods=['POST'])
def convert_webp_to_png():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.webp'):
        return 'Only WebP images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to PNG
    png_image = io.BytesIO()
    image.save(png_image, format='PNG')
    png_image.seek(0)
    
    # create response object with PNG image as attachment
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    
    return response

#pngtowebp converter
@app.route('/api/pngtowebp', methods=['POST'])
def convert_png_to_webp():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.png'):
        return 'Only PNG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to WEBP
    webp_image = io.BytesIO()
    image.save(webp_image, format='WEBP', quality=85)
    webp_image.seek(0)
    
    # create response object with WEBP image as attachment
    response = make_response(webp_image.getvalue())
    response.headers.set('Content-Type', 'image/webp')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.webp')
    
    return response

#bpmtopng converter
@app.route('/api/bmptopng', methods=['POST'])
def convert_bmp_to_png():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.bmp'):
        return 'Only BMP images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to PNG
    png_image = io.BytesIO()
    image.save(png_image, format='PNG')
    png_image.seek(0)
    
    # create response object with PNG image as attachment
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    
    return response

#pngtobmp converter
@app.route('/api/pngtobmp', methods=['POST'])
def convert_png_to_bmp():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.png'):
        return 'Only PNG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to BMP
    bmp_image = io.BytesIO()
    image.save(bmp_image, format='BMP')
    bmp_image.seek(0)
    
    # create response object with BMP image as attachment
    response = make_response(bmp_image.getvalue())
    response.headers.set('Content-Type', 'image/bmp')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.bmp')
    
    return response

#pngtogif converter
@app.route('/api/pngtogif', methods=['POST'])
def convert_png_to_gif():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.png'):
        return 'Only PNG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to GIF
    gif_image = io.BytesIO()
    image.save(gif_image, format='GIF')
    gif_image.seek(0)
    
    # create response object with GIF image as attachment
    response = make_response(gif_image.getvalue())
    response.headers.set('Content-Type', 'image/gif')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.gif')
    
    return response

#giftopng converter

@app.route('/api/giftopng', methods=['POST'])
def convert_gif_to_png():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.gif'):
        return 'Only GIF images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # convert the image to PNG
    png_image = io.BytesIO()
    image.save(png_image, format='PNG')
    png_image.seek(0)
    
    # create response object with PNG image as attachment
    response = make_response(png_image.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.png')
    
    return response

#pngtopdf converter
@app.route('/api/pngtopdf', methods=['POST'])
def convert_png_to_pdf():
    # check if request contains file with 'image' key
    if 'image' not in request.files:
        return 'No image provided', 400
    
    # read the file from 'image' key
    image_file = request.files['image']
    
    # check if the file has allowed extension
    if not image_file.filename.endswith('.png'):
        return 'Only PNG images are allowed', 400
    
    # open the image using PIL
    image = Image.open(io.BytesIO(image_file.read()))
    
    # create PDF file with the image
    pdf_file = io.BytesIO()
    image.save(pdf_file, format='PDF')
    pdf_file.seek(0)
    
    # create response object with PDF file as attachment
    response = make_response(pdf_file.getvalue())
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment', filename='converted_image.pdf')
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
