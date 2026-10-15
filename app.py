from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="reserva_de_hotel",
        user="root",
        password=""
    )
    return conn