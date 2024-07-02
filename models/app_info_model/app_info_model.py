from managers.app import db

class AppInfo(db.Model):
    __tablename__ = "app_info"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, name, description, created_at, updated_at):
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    # def __repr__(self):
    #     return f"<AppInfo {self.name,self.description}>"


