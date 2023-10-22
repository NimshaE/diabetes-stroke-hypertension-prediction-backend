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
                        <h1 class="title">Sign In</h1>

                        <form @submit.prevent="submitForm">
                            <div class="field">
                                <div class="control">
                                    <input type="text" placeholder="Username" class="input" v-model="username">
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <input type="password" placeholder="Password" class="input" v-model="password">
                                </div>
                            </div>

                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>

                            <div class="signup-link" >
                                Forgot Password? &nbsp;<router-link to="/forgotpassword">Click here</router-link>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <button class="button">Sign In</button>
                                </div>
                            </div>
                            <div class="signup-link" >
                                New here?&nbsp;<router-link to="/sign-up">Click here</router-link> 
                            </div>
                            <div class="or-container">
                                <hr class="hr-line">
                                <span class="or-text">Or</span>
                                <hr class="hr-line">
                            </div>
                            <div class="field">
                                <div class="control">
                                    <button class="button">Sign In with Google</button>
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
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | ACTCLINICA'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token

                    localStorage.setItem("token", token)

                    const toPath = this.$route.query.to || '/prediction'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>
