from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root' + \
                                        '@localhost:3306/spm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class JobRoles(db.Model):
    __tablename__ = 'JobRoles'
    JobRole_ID = db.Column(db.String(50), primary_key=True)
    JobRole_Name = db.Column(db.String(50))

db.create_all()

@app.route("/JobRoles")
def JobRole_by_id(JobRole_ID):
    JobRole = JobRoles.query.filter_by(JobRole_ID=JobRole_ID).first()
    if JobRole:
        return jsonify({
            "data": JobRoles.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Job Role not found."
        }), 404












if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)