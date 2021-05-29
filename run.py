from star_tides.create_app import create_app


if __name__ == '__main__':
    host = '0.0.0.0'
    create_app().run(host=host, port=5000)
