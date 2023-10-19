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
          <div class="right-panel">
            <div class="centered-form">
              <div class="column transparent-form">
                <h1 class="title">Predict</h1>
                <h5 class="subhead">Please enter patient data</h5>

                <form @submit.prevent="predict">
                  <div class="field is-grouped">
                      <div class="control">
                          <input type="text" placeholder="Age" class="input" v-model="formData.age">
                      </div>
                      <div class="control">
                        <div class="input custom-select">
                            <select v-model="formData.sex">
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                            </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                    <div class="control">
                      <div class="input custom-select">
                            <select v-model="formData.highChol">
                                <option value="high">High</option>
                                <option value="low">Low</option>
                            </select>
                      </div>
                    </div>
                    <div class="control">
                          <input type="text" placeholder="BMI" class="input" v-model="formData.bmi">
                    </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        <div class="input custom-select">
                              <select v-model="formData.smoker">
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                        <div class="input custom-select">
                              <select v-model="formData.heartDiseaseorAttack">
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        <div class="input custom-select">
                              <select v-model="formData.physActivity">
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                        <div class="input custom-select">
                              <select v-model="formData.hvyAlcoholConsump">
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        <div class="input custom-select">
                              <select v-model="formData.genHlth">
                                  <option value="weak">Weak</option>
                                  <option value="low">Low</option>
                                  <option value="neutral">Neutral</option>
                                  <option value="good">Good</option>
                                  <option value="High">High</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                          <input type="text" placeholder="Mentalhealth" class="input" v-model="formData.mentHlth">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <button class="button">Submit</button>
                      </div>
                  </div>
                  
                  <Result :predictions="predictions" />
                </form>
                <p class="has-text-danger">{{ formError }}</p>
              </div>
            </div>
          </div>
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      formData: {
        age: null,
        sex: null,
        highChol: null,
        bmi: null,
        smoker: null,
        heartDiseaseorAttack: null,
        physActivity: null,
        hvyAlcoholConsump: null,
        genHlth: null,
        mentHlth: null
      },
      ageError: '',
      bmiError: '',
      mentHlthError: '',
      formError: '',
    };
  },
  methods: {
    isValidInteger(value) {
      // Helper function to check if a value is a valid integer
      return /^\d+$/.test(value);
    },
    mapAgeToGroup(age) {
      if (age >= 18 && age <= 24) {
        return 1;
      } else if (age >= 25 && age <= 29) {
        return 2;
      }
      else if (age >= 25 && age <= 29) {
        return 3;
      }
      else if (age >= 30 && age <= 34) {
        return 4;
      }
      else if (age >= 35 && age <= 39) {
        return 5;
      }
      else if (age >= 40 && age <= 44) {
        return 6;
      }
      else if (age >= 45 && age <= 49) {
        return 7;
      }
      else if (age >= 50 && age <= 54) {
        return 8;
      }
      else if (age >= 55 && age <= 59) {
        return 9;
      }
      else if (age >= 60 && age <= 64) {
        return 10;
      }
      else if (age >= 65 && age <= 69) {
        return 11;
      }
      else if (age >= 70 && age <= 74) {
        return 12;
      }
      else if (age >= 75 && age <= 80) {
        return 13;
      }
      if (age > 80)
      {
        return 14;
      }
    },
    mapGenHlthValue(selectedValue) {
      // Define a mapping from selected values to numeric values (1 to 5)
      const valueMapping = {
        'weak': 1,
        'low': 2,
        'neutral': 3,
        'good': 4,
        'High': 5,
      };

      // Map the selected value to a numeric value
      return valueMapping[selectedValue];
    },
    async predict() {  
      
      this.formError = '';

      if (!this.formData.age) {
        this.ageError = 'Age is required.';
      } else if (!this.isValidInteger(this.formData.age)) {
        this.ageError = 'Age must be an integer.';
      } else {
        this.ageError = '';
      }

      if (!this.formData.bmi) {
        this.bmiError = 'BMI is required.';
      } else if (!this.isValidInteger(this.formData.bmi)) {
        this.bmiError = 'BMI must be an integer.';
      } else {
        this.bmiError = '';
      }

      if (!this.formData.mentHlth) {
        this.mentHlthError = 'Mental health is required.';
      } else if (!this.isValidInteger(this.formData.mentHlth)) {
        this.mentHlthError = 'Mental health must be an integer.';
      } else {
        this.mentHlthError = '';
      }

      // Check if any errors occurred, and if so, don't proceed with the Axios request
      if (this.ageError || this.bmiError || this.mentHlthError) {
        this.formError = 'Please fix the errors in the form.';
        return;
      }

      const sexValue = this.formData.sex === 'male' ? 1 : 0;
      const cholValue = this.formData.highChol === 'high' ? 1 : 0;
      const smokeValue = this.formData.smoker === 'yes' ? 1 : 0;
      const heartValue = this.formData.heartDiseaseorAttack === 'yes' ? 1 : 0;
      const phyValue = this.formData.physActivity === 'yes' ? 1 : 0;
      const alcoValue = this.formData.hvyAlcoholConsump === 'yes' ? 1 : 0;
      const ageGroup = this.mapAgeToGroup(this.formData.age);

      const formData = {
        Age: this.formData.age,
        Sex: sexValue, 
        HighChol: cholValue,
        BMI: this.formData.bmi,
        Smoker: smokeValue,
        HeartDiseaseorAttack: heartValue,
        PhysActivity: phyValue,
        HvyAlcoholConsump: alcoValue,
        GenHlth: this.mapGenHlthValue(this.formData.genHlth),
        MentHlth: this.formData.mentHlth
      };
      try {
        const response = await axios.post('/api/v1/predictions/', formData);
        this.$router.push({ name: 'results', query: { predictions: JSON.stringify(response.data) } });
      } catch (error) {
        console.error('Prediction failed:', error);
      }
    },
  }, 
  mounted(){
    document.title = 'Predict | ACTCLINICA'
  },
};
</script>
<style lang="scss">
html, body {
  overflow: hidden;
  height: 100%;
  margin: 0;
  padding: 0;
}
.page-prediction {
  position: relative;
  height: 100vh; 
  overflow: hidden;
}
.bg-prediction {
    background-image: url('../assets/bg-image.png');
    background-size: cover;
    background-position: center;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

</style>