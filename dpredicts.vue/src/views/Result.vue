<template>
    <div class="page-prediction bg-prediction">
        <div class="content">
            <div class="left-panel">
                <div class="centered-panel-content">
                    <h1>ACTCLINICA</h1>
                    <h5>To a better life</h5>

                    <router-link to="/result-list" class="navbar-item">Reports</router-link>
                    <template v-if="$store.state.isAuthenticated">
                      <router-link to="/my-account" class="button is-light">My account</router-link>
                    </template>
                    <template v-else>
                        <router-link to="/log-in"><button class="button">Log Out</button></router-link>
                    </template>
                </div>
            </div>
            <div class="right-panel">
              <div class="centered-form">
                <div class="column transparent-form">
                  <h1 class="title">Prediction Results</h1>
                  <h3 style="color: #2F80ED">
                      {{ currentDateTime }}
                  </h3>
                  <div class="prediction" v-if="parsedPredictions">
                    <h5>Diabetes Prediction:  {{ parsedPredictions.Diabetes }}</h5>
                    <h5>Hypertension Prediction: {{ parsedPredictions.Hypertension }}</h5>
                    <h5>Stroke Prediction: {{ parsedPredictions.Stroke }}</h5>
                  </div>
                  <form @submit.prevent="submitForm">
                    <div class="field">
                        <div class="control">
                            <input type="text" placeholder="Patient Name" class="input" v-model="patientName">
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <input type="text" placeholder="Note" class="input" v-model="note">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button">Submit</button>
                        </div>
                    </div>
                  
                  </form>

                </div>

              </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {},
  data() {
    return {
      parsedPredictions: {},
      currentDateTime: "",
      patientName: '', 
      note: '', 
    };
  },
  created() {
    const predictionsString = this.$route.query.predictions;
    if (predictionsString) {
      try {
        this.parsedPredictions = JSON.parse(predictionsString);
      } catch (error) {
        console.error('Failed to parse predictions:', error);
      }
    }

    this.updateCurrentDateTime();
  },
  methods: {
    updateCurrentDateTime() {
      const now = new Date();
      const options = { year: 'numeric', month: 'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: true };
      this.currentDateTime = now.toLocaleDateString('en-US', options);
    },
    submitForm() {
      const data = {
        patient_name: this.patientName,
        note: this.note,
        diabetes_prediction: this.parsedPredictions.Diabetes,
        hypertension_prediction: this.parsedPredictions.Hypertension,
        stroke_prediction: this.parsedPredictions.Stroke,
        prediction_timestamp: this.currentDateTime,
      };

      axios
        .post('/api/v1/results/', data)
        .then((response) => {
          console.log('Data saved successfully:', response.data);
          this.$router.push({ name: 'Prediction' }); 
        })
        .catch((error) => {
          console.error('Error saving data:', error);
        });
    },
  },
  mounted() {
    document.title = 'Results | ACTCLINICA';
  },
};
</script>
<style lang="scss">

</style>
  