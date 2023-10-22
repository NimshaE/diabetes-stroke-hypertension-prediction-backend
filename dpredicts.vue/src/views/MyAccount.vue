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
                <div>
                    <img src="../assets/Vector.png"/>
                </div>
                <div class="column">
                  <h1 class="title">My Account</h1>
                  <div class="account">
                    <h5>Username: {{ user.username }} </h5>
                    <h5>Email: {{ user.email }}</h5>
                  </div>
                  <form>
                    <div class="field">
                        <div class="control">
                            <button @click="logout()" class="button">Log out</button>
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
    name: 'MyAccount',
    components: {
    },
    data() {
        return {
            user: {
                username: '',
                email: '',
            },
        }
    },
    mounted() {
        document.title = 'My Account | ACTCLINICA'
        axios.get('/api/v1/profile/')
            .then(response => {
                this.user = response.data;
            })
            .catch(error => {
                console.error('Error fetching user profile:', error);
            });
    },
    methods: {
        logout() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")

            this.$store.commit('removeToken')

            this.$router.push('/')
        },   
    }
}
</script>