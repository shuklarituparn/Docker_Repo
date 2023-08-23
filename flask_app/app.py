from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
   "https://masterpiecer-images.s3.yandex.net/a230962f417011eebda4ca697c28bd51:upscaled",
    "https://masterpiecer-images.s3.yandex.net/1f3cad6241bb11ee8084c2e644eb6d3f:upscaled",
    "https://masterpiecer-images.s3.yandex.net/5faa0f9987df85d:upscaled",
    "https://masterpiecer-images.s3.yandex.net/5fadcaff2e5d4a8:upscaled",
    "https://masterpiecer-images.s3.yandex.net/5fe10c060b980c2:upscaled",
    "https://masterpiecer-images.s3.yandex.net/5f893b407c97d44:upscaled",
    "https://masterpiecer-images.s3.yandex.net/5fa25b633f3fed1:upscaled",
    "https://masterpiecer-images.s3.yandex.net/e5e66d4c417b11ee81b09a793c1e62bc:upscaled"


]

@app.route('/')  # This is a decorator that associates a function with a URL route. In this case, it associates the index() function with the root URL '/'
def index():
    url=random.choice(images)
    return render_template('index.html', url=url)

if __name__=="__main__":  #his is the function that will be executed when the root URL is accessed
    app.run(host="0.0.0.0")   #0.0.0.0 Means that the program can listen on any of the ip address
