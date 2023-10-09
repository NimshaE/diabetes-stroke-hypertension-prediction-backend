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
                <h1 class="title">Predict</h1>
                <h5 class="subhead">Please enter patient data</h5>

                <form @submit.prevent="predict">
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Age" class="input" v-model="formData.age">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Sex" class="input" v-model="formData.sex">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Cholesterol Status" class="input" v-model="formData.highChol">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="BMI" class="input" v-model="formData.bmi">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="A smoker" class="input" v-model="formData.smoker">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Heart patient?" class="input" v-model="formData.heartDiseaseorAttack">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Active?" class="input" v-model="formData.physActivity">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Alchoholic?" class="input" v-model="formData.hvyAlcoholConsump">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Generalhealth" class="input" v-model="formData.genHlth">
                      </div>
                  </div>
                  <div class="field">
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
    };
  },
  methods: {
    async predict() {
      const formData = {
        Age: this.formData.age,
        Sex: this.formData.sex,
        HighChol: this.formData.highChol,
        BMI: this.formData.bmi,
        Smoker: this.formData.smoker,
        HeartDiseaseorAttack: this.formData.heartDiseaseorAttack,
        PhysActivity: this.formData.physActivity,
        HvyAlcoholConsump: this.formData.hvyAlcoholConsump,
        GenHlth: this.formData.genHlth,
        MentHlth: this.formData.mentHlth
      };
      try {
        const response = await axios.post('/api/v1/predictions/', formData);
        // After prediction, redirect to the result page with predictions as a string
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