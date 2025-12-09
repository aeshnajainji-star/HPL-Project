# Real-Time Supply Chain Visibility & ETA Prediction System

This project is created for **Hacker's Premier League (HPL) Round 1** by Guru Gobind Singh Indraprastha University (GGSIPU), Delhi.

---

## Team Name: CipherSages

**Team Members:**
-  Aeshna Jain — GPS Simulator & Backend  
- Riddhima Baliyan Backend & ETA Calculation  
- Parul Singh Frontend & Map UI  
- Manya Jain AI Assistant & Demo Video

---

## Project Overview

The goal of this project is to build a **real-time supply chain tracking system** that allows logistics companies to monitor vehicle locations, calculate estimated time of arrival (ETA), and generate alerts for route deviations. It also includes a lightweight AI assistant for querying vehicle locations and ETAs.

---

## Features

- **Real-time GPS Tracking:** Vehicles simulated using a GPS simulator, sending data every second.  
- **Dynamic ETA Calculation:** Backend calculates distance to destination and estimated arrival time based on speed.  
- **Frontend Map UI:** Shows vehicle movement on a live map with real-time ETA popups.  
- **Alerts:** Detects slow speed or route deviations.  
- **AI Assistant:** Answers queries like "Where is vehicle V1?" or "What is the ETA?".

---

## Project Structure
---

## How to Run the Project

### 1. Backend
1. Open a command prompt (CMD) and go to the backend folder:
cd" C:\Users\Aeshna\OneDrive\Desktop\HPL-Project\Backend"
2. Run the backend server:
python app.py
- The backend will start and show:
Running on http://127.0.01:500/
---

### 2. Simulator
1. Open a **new CMD window**.  
2. Go to the simulator folder:
cd" C:\Users\Aeshna\OneDrive\Desktop\HPL-Project\Backend"
3. Run the simulator:
python simulate.py
- You will see live data being sent every second.  
- Backend CMD window will show `POST /update HTTP/1.1" 200 -` indicating successful data reception.

---

### 3. Frontend
1. Open the `index.html` file from the Frontend folder in a browser.  
2. You will see a map with a moving vehicle marker.  
3. Clicking the marker shows the ETA and alerts.

---

## Libraries & Tools Used

- Python 3.12  
- Flask (for backend API)  
- Geopy (for distance and ETA calculation)  
- Leaflet.js (for frontend map UI)  
- HTML/CSS/JavaScript (frontend)  
- Optional: Lightweight LLM API for AI Assistant

---

## How the Team Worked

- **Member A (Aeshna):** Created GPS Simulator & Backend  
- **Member B (Riddhima Baliyan):** Helped with Backend & ETA calculation  
- **Member C(Parul Singh):** Developed the Frontend Map UI  
- **Member D(Manya Jain):** Developed AI Assistant & recorded demo video

---

## Demo Video Script Summary

- **0:00 – 0:07:** Title screen with project name, team, and college  
- **0:07 – 0:20:** Member D introduction and project overview  
- **0:20 – 0:45:** Member A explains GPS Simulator  
- **0:45 – 1:15:** Member B explains Backend & ETA calculation  
- **1:15 – 1:50:** Member C explains Frontend Map UI  
- **1:50 – 2:10:** Member D shows AI Assistant  
- **2:10 – 2:25:** Closing remarks, full system overview

---

## Submission Notes

- Keep backend running before starting simulator and frontend.  
- Demo video can be recorded showing all members explaining their parts.  
- Upload the full project folder to GitHub with the above structure.  
- Share the GitHub repository link and video link in the submission form.

---

## Contact

For any queries regarding the project:

 Aeshna Jain — [aeshnajainji@gmail.com]
# HPL-Project
GGSIPU HPL Round 1 - Real-Time Supply Chain Tracking System
