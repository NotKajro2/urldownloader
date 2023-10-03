from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'downloads/%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_path = ydl.prepare_filename(info)

                if video_path.endswith(".mp4"):
                    filename = info['title'] + ".mp4"

                    response = send_file(
                        video_path,
                        as_attachment=True,
                        download_name=filename,
                        mimetype='video/mp4'
                    )

                    return response
                else:
                    return "No MP4 video found for this URL."

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
