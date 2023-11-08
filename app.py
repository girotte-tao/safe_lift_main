from app import app, db

if __name__ == '__main__':
    # 启动flask
    with app.app_context():
        db.create_all()
        app.run()