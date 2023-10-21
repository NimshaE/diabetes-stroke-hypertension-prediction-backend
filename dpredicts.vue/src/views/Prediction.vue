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
                    <h5><router-link to="/my-account">My Account</router-link></h5>
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
                        Age Group
                          <div class="input custom-select">
                            <select v-model="formData.age" required>
                                <option value="one">18-24</option>
                                <option value="two">25-29</option>
                                <option value="three">30-34</option>
                                <option value="four">35-39</option>
                                <option value="five">40-44</option>
                                <option value="six">45-49</option>
                                <option value="seven">50-54</option>
                                <option value="eight">55-59</option>
                                <option value="nine">60-64</option>
                                <option value="ten">65-69</option>
                                <option value="eleven">70-74</option>
                                <option value="twelve">75-79</option>
                                <option value="thirteen">80+</option>
                            </select>
                        </div>
                      </div>
                      <div class="control">
                        Gender
                        <div class="input custom-select">
                            <select v-model="formData.sex" required>
                                <option value="male">Male</option>
                                <option value="female">Female</option>
                            </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                    <div class="control">
                      Cholesterol Status
                      <div class="input custom-select">
                            <select v-model="formData.highChol" required>
                                <option value="high">High</option>
                                <option value="low">Low</option>
                            </select>
                      </div>
                    </div>
                    <div class="control">
                      BMI
                          <input type="text" class="input" v-model="formData.bmi" required>
                    </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        Smoking Status
                        <div class="input custom-select">
                              <select v-model="formData.smoker">
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                        History of Heart Disease
                        <div class="input custom-select">
                              <select v-model="formData.heartDiseaseorAttack" required>
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        Physical Exercises
                        <div class="input custom-select">
                              <select v-model="formData.physActivity" required>
                                  <option value="yes">Yes</option>
                                  <option value="no">No</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                        Alcohol Consumption
                        <div class="input custom-select">
                              <select v-model="formData.hvyAlcoholConsump" required>
                                  <option value="yes">High</option>
                                  <option value="no">Low</option>
                              </select>
                        </div>
                      </div>
                  </div>
                  <div class="field is-grouped">
                      <div class="control">
                        General Health
                        <div class="input custom-select">
                              <select v-model="formData.genHlth" required>
                                <option value="weak">Weak</option>
                                <option value="low">Low</option>
                                <option value="neutral">Neutral</option>
                                <option value="good">Good</option>
                                <option value="high">High</option>
                              </select>
                        </div>
                      </div>
                      <div class="control">
                        Mental Health
                        <div class="input custom-select">
                          <select v-model="formData.mentHlth" required>
                            <option value="extreme">Extreme Distress</option>
                            <option value="severe">Severe Mental Concerns</option>
                            <option value="moderate">Moderate Mental Concerns</option>
                            <option value="some">Some Challenges</option>
                            <option value="neutral">Neutral</option>
                            <option value="good">Good Mentality</option>
                            <option value="verygood">Very Good Mentality</option>
                            <option value="excellent">Excellent Mentality</option>
                            <option value="peak"> Peak Mentality</option>
                            <option value="perfect">Perfect Mentality</option>
                          </select>
                        </div>
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
      return /^\d+$/.test(value);
    },
    mapAgeToGroup(selected) {
      const valueMapping = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
      };
      return valueMapping[selected];
    },
    mapGenHlthValue(selectedValue) {
      const valueMapping = {
        'weak': 1,
        'low': 2,
        'neutral': 3,
        'good': 4,
        'high': 5,
      };
      return valueMapping[selectedValue];
    },
    mapMenHlthValue(option) {
      const valueMapping = {
        'extreme': 1,
        'severe': 2,
        'moderate': 3,
        'some': 4,
        'neutral': 5,
        'good': 6,
        'verygood': 7,
        'excellent': 8,
        'peak': 9,
        'perfect': 10,
      };
      return valueMapping[option];
    },
    async predict() {  
      
      this.formError = '';

      if (!this.formData.bmi) {
        this.bmiError = 'BMI is required.';
      } else if (!this.isValidInteger(this.formData.bmi)) {
        this.bmiError = 'BMI must be an integer.';
      } else {
        this.bmiError = '';
      }

      // Check if any errors occurred, and if so, don't proceed with the Axios request
      if (this.bmiError) {
        this.formError = 'Please fix the errors in the form.';
        return;
      }

      const sexValue = this.formData.sex === 'male' ? 1 : 0;
      const cholValue = this.formData.highChol === 'high' ? 1 : 0;
      const smokeValue = this.formData.smoker === 'yes' ? 1 : 0;
      const heartValue = this.formData.heartDiseaseorAttack === 'yes' ? 1 : 0;
      const phyValue = this.formData.physActivity === 'yes' ? 1 : 0;
      const alcoValue = this.formData.hvyAlcoholConsump === 'yes' ? 1 : 0;

      const formData = {
        Age: this.mapAgeToGroup(this.formData.age),
        Sex: sexValue, 
        HighChol: cholValue,
        BMI: this.formData.bmi,
        Smoker: smokeValue,
        HeartDiseaseorAttack: heartValue,
        PhysActivity: phyValue,
        HvyAlcoholConsump: alcoValue,
        GenHlth: this.mapGenHlthValue(this.formData.genHlth),
        MentHlth: this.mapMenHlthValue(this.formData.mentHlth)
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