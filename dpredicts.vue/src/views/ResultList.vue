<template>
    <div class="page-prediction bg-prediction">
        <div class="content">
            <div class="left-panel">
                <div class="centered-panel-content">
                    <h1>ACTCLINICA</h1>
                    <h5>To a better life</h5>
                    <template v-if="$store.state.isAuthenticated">
                    <h5><router-link to="/prediction">Predict</router-link></h5>
                  </template>
                  <template v-if="$store.state.isAuthenticated">
                    <h5><router-link to="/result-list">Report</router-link></h5>
                  </template>
                  <template v-if="$store.state.isAuthenticated">
                    <h5><router-link to="/my-account">My account</router-link></h5>
                  </template>
                  <template v-else>
                      <h5><router-link to="/log-in">Log Out</router-link></h5>
                  </template>
                </div>
            </div>
            <div class="right-panel ">
                <div class="date-filter">
                    <label for="fromDate">From:</label>
                    <input type="date" id="fromDate" v-model="fromDate">
                    <label for="toDate">To:</label>
                    <input type="date" id="toDate" v-model="toDate">
                    <button @click="filterResults">Apply Filter</button>
                    <button @click="exportToCSV">Export Data</button>
                </div>
                <div class="result-table">
                    <table>
                        <thead>
                        <tr>
                            <th>Patient</th>
                            <th>Diabetes</th>
                            <th>Hypertension</th>
                            <th>Stroke</th>
                            <th>Note</th>
                            <th>Date & Time</th>
                        </tr>
                        </thead>
                        <tbody>
                            <tr v-for="result in results" :key="result.id">
                                <td>{{ result.patient_name }}</td>
                                <td>{{ result.diabetes_prediction }}</td>
                                <td>{{ result.hypertension_prediction }}</td>
                                <td>{{ result.stroke_prediction }}</td>
                                <td>{{ result.note }}</td>
                                <td>{{ formatTimestamp(result.prediction_timestamp) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    
  </template>
  
<script>
  import axios from 'axios';
  import Papa from 'papaparse'; 
  
  export default {
    data() {
      return {
        results: [],
        fromDate: '', 
        toDate: '',
      };
    },
    mounted() {
      axios
        .get('/api/v1/results/')
        .then((response) => {
          this.results = response.data;
        })
        .catch((error) => {
          console.error('Error fetching results:', error);
        });
    },
    methods: {
      formatTimestamp(timestamp) {
        const date = new Date(timestamp);
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        return `${year}-${month}-${day} ${hours}:${minutes}`;
      },
      filterResults() {
                if (!this.fromDate || !this.toDate) {
                // Add some error handling or feedback to the user
                return;
            }
            const fromDate = new Date(this.fromDate);
            const toDate = new Date(this.toDate);
            this.results = this.results.filter((result) => {
            const resultDate = new Date(result.prediction_timestamp);
            return resultDate >= fromDate && resultDate <= toDate;
            });
        },
        exportToCSV() {
            const filteredData = this.results.map((result) => ({
            PatientName: result.patient_name,
            DiabetesPrediction: result.diabetes_prediction,
            HypertensionPrediction: result.hypertension_prediction,
            StrokePrediction: result.stroke_prediction,
            Note: result.note,
            Timestamp: this.formatTimestamp(result.prediction_timestamp),
            }));

            const csv = Papa.unparse(filteredData, { header: true });

            const blob = new Blob([csv], { type: 'text/csv' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'filtered_results.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        },
    },
};
</script>
  
<style scoped>
.navbar-item:hover {
    border-radius: 20px;
    color: #2F80ED;
    background-color: none;
}
.right-panel {
  margin: 40px;
}
  .result-table {

  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, 
  td {
    border: 1px solid #ccc;
    font-weight: 600;
    padding: 8px;
    text-align: left;
  }
  
  thead {
    background-color: rgba(255, 255, 255, 0.5);
  }

  .date-filter {
  display: flex;
  align-items: center;
  margin-bottom: 20px; 
}

label {
  margin-right: 10px;
}

input[type="date"] {
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-right: 10px;
}
.date-filter button {
  border-radius: 25px;
  color: white;
  background-color: #2F80ED;
  padding: 7px;
  margin: 5px;
  border: none;
}
.date-filter button:hover {
  border-radius: 25px;
  color: #2F80ED;
  background-color: white;
  border-color: #2F80ED;
  font-weight: bold;
}</style>
  
