<template>
    <div class="page-prediction bg-prediction">
        <div class="content">
          <div class="left-panel">
              <div class="centered-panel-content">
                  <h1>ACTCLINICA</h1>
                  <h5>To a better life</h5>
              </div>
          </div>
          <div class="right-panel">
            <div class="centered-form">
              <div class="column predict-form">
                <h1 class="title">Predict</h1>
                <h5>Please enter patient data</h5>

                <form>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Age" class="input" v-model="age">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Sex" class="input" v-model="sex">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Cholesterol Status" class="input" v-model="chol">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="BMI" class="input" v-model="bmi">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="A smoker" class="input" v-model="smoke">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Heart patient?" class="input" v-model="heart">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Active?" class="input" v-model="physical">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Alchoholic?" class="input" v-model="alcohol">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Generalhealth" class="input" v-model="health">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Mentalhealth" class="input" v-model="mentalh">
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
.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
}
.left-panel {
  width: 30%;
  background-color: rgba(255, 255, 255, 0.5);
  height: 100%;
}
.centered-panel-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.right-panel {
  width: 70%;
}
.centered-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
}
.predict-form {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 15px;
  width: 80%;
  max-width: 400px;
}
</style>