import argparse
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello , India!"

def parse_args():
    parser = argparse.ArgumentParser(description='A simple example program to print a friendly greeting and start a server.')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
    parser.add_argument('--version', action='version', version='helloworld ' + '1.0.0')  # Replace '1.0.0' with actual version
    return parser.parse_args()

def main(argv=None):
    if argv is None:
        argv = sys.argv

    args = parse_args()

    # If the --port argument is provided, start the Flask server
    if '--port' in argv:
        app.run(host='0.0.0.0', port=args.port)
    else:
        print("Hello, India")

    return 0

if __name__ == '__main__':
    sys.exit(main())
