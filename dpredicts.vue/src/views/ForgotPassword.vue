<template>
    <div class="page-log-in background-image">
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
                        <h1 class="title">Forgot Password</h1>

                        <form  @submit.prevent="checkEmailAndRedirect">
                            <div class="field">
                                <div class="control">
                                    <input type="email" placeholder="Email" class="input" v-model="email">
                                </div>
                            </div>

                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button">Send Recovery Link</button>
                                </div>
                            </div>
                            <div class="signup-link" >
                                &nbsp;<router-link to="/sign-up">Back to Sign In</router-link>
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
  data() {
    return {
      email: '',
      errors: [],
    };
  },
  methods: {
    async checkEmailAndRedirect() {
      this.errors = [];

      try {
        const response = await axios.post('/api/v1/check-email/', { email: this.email });
        if (response.data.exists) {
            this.resetToken = response.data.reset_token; 
            this.$router.push({ name: 'update-password', params: { email: this.email } });
        } else {
            this.errors.push('Email not found. Please check the email address.');
        }
        } catch (error) {
            this.errors.push('An error occurred. Please try again later.');
        }
    },
  },
};
</script>
