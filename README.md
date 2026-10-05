# DRDO Smart Scan

## AI-Based Adaptive RF Threat Detection for Electronic Warfare

DRDO Smart Scan is a Python and Streamlit based project developed to demonstrate an adaptive RF spectrum scanning system.

The project creates a simulated RF environment and monitors different frequency bands. It compares traditional scanning with a smart scanning approach and displays possible threats through a simple dashboard.

This project is mainly developed for academic, project demonstration and hackathon purposes. It uses simulated RF data and does not directly connect to or control real electronic warfare equipment.

## Features

### RF Spectrum Monitoring

The system generates simulated RF spectrum data and displays the signal activity for 50 different bands.

The spectrum is shown using a bar chart so that active signal bands can be easily identified.

### Scanning Modes

The dashboard provides three scanning modes:

- Passive Scan
- Active Scan
- AI Smart Scan

The scanning mode can be selected from the sidebar.

### Threat Level

The user can select the required threat level:

- Low
- Medium
- High

### Traditional and Smart Scanning

The project compares traditional scanning with smart scanning.

The two scanner classes used in the project are:

```text
TraditionalScanner
SmartScanner
```

The number of detected hits from both methods is displayed on the dashboard for comparison.

### Threat Detection

The dashboard displays some simulated RF threats such as:

| Emitter | Threat Level | Band |
|---|---|---|
| Enemy Radar | HIGH | 12 |
| Drone Link | MEDIUM | 25 |
| Command Radio | LOW | 40 |

These are simulated values used for demonstrating the working of the dashboard.

### AI Recommendation

The system checks the active frequency bands and gives a recommendation for the next band to scan.

For example:

```text
Recommended Next Scan Band: 12
```

### EW Metrics

The dashboard also shows some example electronic warfare metrics:

- Detection Probability: 91%
- False Alarm Rate: 8%
- Interception Rate: 89%

These values are used for the project demonstration.

## How the System Works

The basic working flow of the project is:

```text
RF Environment
       |
       v
Generate Spectrum Data
       |
       v
Detect Signal Activity
       |
       v
Analyze Frequency Bands
       |
       v
Compare Traditional and Smart Scan
       |
       v
Identify Possible Threats
       |
       v
Recommend Next Scan Band
       |
       v
Display Results on Dashboard
```

The main idea is to avoid treating all frequency bands in exactly the same way. The smart scan focuses more on bands where signal activity is detected.

## Project Structure

```text
EW_Dashboard/
│
├── app.py
├── simulator.py
├── scanner.py
├── requirements.txt
└── venv/
```

### app.py

This is the main Streamlit application. It contains the dashboard interface, spectrum graph, threat information, comparison charts and system metrics.

### simulator.py

This file contains the RF environment simulation.

It provides:

```python
RFEnvironment
```

### scanner.py

This file contains the scanning classes:

```python
TraditionalScanner
SmartScanner
```

### requirements.txt

This file contains the Python packages required to run the project.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly

Plotly is used for displaying the RF spectrum and comparison charts.

## Installation

### 1. Open PowerShell

Go to the project folder:

```powershell
cd "C:\Users\Deekshith\OneDrive\Pictures\Desktop\EW_Dashboard"
```

### 2. Create Virtual Environment

If the virtual environment is not already available:

```powershell
python -m venv venv
```

### 3. Activate the Environment

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(venv) PS C:\Users\Deekshith\OneDrive\Pictures\Desktop\EW_Dashboard>
```

### 4. Install Required Packages

```powershell
python -m pip install -r requirements.txt
```

## Running the Project

Start the Streamlit application using:

```powershell
python -m streamlit run app.py
```

After starting the application, Streamlit normally provides the following local URL:

```text
http://localhost:8501
```

Open this address in a web browser.

If port 8501 is already being used, another port can be specified:

```powershell
python -m streamlit run app.py --server.port 8502
```

Then open:

```text
http://localhost:8502
```

## Dashboard

The dashboard contains:

- Control panel
- Scanning mode selection
- Threat level selection
- Active emitter information
- Threat count
- Scan success information
- Live RF spectrum
- Traditional vs smart scan comparison
- Detected threat table
- Threat distribution chart
- AI scan recommendation
- EW performance metrics
- System activity log

## System Architecture

```text
             Streamlit Dashboard
                     |
                     v
             RF Environment
                Simulator
                     |
                     v
              RF Spectrum
                     |
          +----------+----------+
          |                     |
          v                     v
 Traditional Scanner      Smart Scanner
          |                     |
          +----------+----------+
                     |
                     v
              Threat Analysis
                     |
                     v
             Scan Recommendation
                     |
                     v
              Dashboard Output
```

## Future Improvements

The project can be extended in the future with:

- SDR hardware integration
- Real-time spectrum data
- Frequency waterfall display
- Signal classification
- Anomaly detection
- Dynamic scan scheduling
- Signal priority calculation
- Historical signal analysis
- Threat confidence scores
- Real-time alerts

A possible future hardware flow is:

```text
SDR
 |
 v
RF Signal Acquisition
 |
 v
Spectrum Processing
 |
 v
Smart Scan Algorithm
 |
 v
Threat Classification
 |
 v
Dashboard
```

## Limitations

The current project uses simulated RF data rather than real RF signals.

The threat information and EW metrics shown on the dashboard are demonstration values.

The project is not intended for real-world RF jamming, interception or weapon-control applications.
