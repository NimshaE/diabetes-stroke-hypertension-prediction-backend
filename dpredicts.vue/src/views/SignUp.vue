<template>
    <div class="page-sign-up background-image">
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
                        <h1 class="title">Sign up</h1>
                        <h5>
                            Already have an account?&nbsp;<router-link to="/log-in">click here</router-link>
                        </h5>
                        <form @submit.prevent="submitForm">
                            <div class="field">
                                <div class="control">
                                    <input type="text" placeholder="Username" class="input" v-model="username">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input type="text" placeholder="Center Name" class="input" v-model="centerName">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input type="email" placeholder="Email" class="input" v-model="email">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input type="password" placeholder="Password" class="input" v-model="password">
                                </div>
                            </div>
                            <div class="field">
                                <div class="control">
                                    <input type="password" placeholder="Repeat password" class="input" v-model="password2">
                                </div>
                            </div>

                            <div class="notification is-danger" v-if="errors.length">
                                <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button">Sign up</button>
                                </div>
                            </div>
                            <div class="or-container">
                                <hr class="hr-line">
                                <span class="or-text">Or</span>
                                <hr class="hr-line">
                            </div>
                            <div class="field">
                                <div class="control">
                                    <button class="button">Sign Up with Google</button>
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
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            centerName: '',
            email: '',
            errors: [],
            showPassword: false,
        }
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The Fullname is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }
            if (this.centerName === '') {
                this.errors.push('Centre name is required');
            }
            if (this.email === '' || !this.isValidEmail(this.email)) {
                this.errors.push('Invalid or missing email');
            }
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password,
                    centerName: this.centerName,
                    email: this.email
                }

                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        toast({
                            message: 'Account created, please log in!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        },
        isValidEmail(email) {
            const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
            return emailRegex.test(email);
        }
    }
}
</script>