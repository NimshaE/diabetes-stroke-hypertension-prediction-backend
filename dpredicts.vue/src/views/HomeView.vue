<template>
  <div class="background-image">
    <div class="content">
      <div class="left-panel">
          <div class="centered-panel-content">
              <h1>ACTCLINICA</h1>
              <h5>To a better life</h5>
          </div>
      </div>
      <div class="right-panel">
          <div class="centered-form">
              <div class="column transparent-form">
                  <h1 class="title">Start Your Analysation</h1>
                  <form>
                    <router-link to="/sign-up">
                      <div class="field">
                          <div class="control">
                              <button class="button">Sign Up Now!</button>
                          </div>
                      </div>
                    </router-link>
                      
                      
                      <div class="or-container">
                          <hr class="hr-line">
                          <span class="or-text">Or</span>
                          <hr class="hr-line">
                      </div>

                      <div class="hyper-link" >
                        <h5>
                          Already have an account?&nbsp;<router-link to="/log-in">Sign In</router-link>
                        </h5>
                      </div>
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
  name: 'HomeView',
  data(){
    return{
    }
  },
  components: {  
  },
  mounted(){
    document.title = 'Home | ACTCLINICA'
  },
  methods: {
  }
}
</script>
