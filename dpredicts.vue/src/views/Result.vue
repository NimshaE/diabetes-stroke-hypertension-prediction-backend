<!--<template>
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
                          <input type="text" placeholder="Diabetes state:" class="input" v-model="diabetes">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Hypertension state:" class="input" v-model="hypertension">
                      </div>
                  </div>
                  <div class="field">
                      <div class="control">
                          <input type="text" placeholder="Stroke state:" class="input" v-model="stroke">
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
</template>-->
<!-- result.vue -->
<template>
  <div class="result-page">
    <h1 class="title">Prediction Results</h1>

    <div class="prediction" v-if="parsedPredictions">
      <p>Diabetes Prediction: {{ parsedPredictions.Diabetes }}</p>
      <p>Hypertension Prediction: {{ parsedPredictions.Hypertension }}</p>
      <p>Stroke Prediction: {{ parsedPredictions.Stroke }}</p>
    </div>
  </div>
</template>
  
<script>
export default {
  props: {
  },
  data() {
    return {
      parsedPredictions: {}, // Initialize parsedPredictions as an empty Object
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
},
};
</script>

  