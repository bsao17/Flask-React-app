import server
import config_database


if __name__ == '__main__':
    server.app.run(debug=True)