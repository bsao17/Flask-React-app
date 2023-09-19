import server
import __init__


if __name__ == '__main__':
    __init__.create_connection()
    server.app.run(debug=True)