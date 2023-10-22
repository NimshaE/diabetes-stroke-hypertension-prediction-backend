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
                        <h1 class="title">Change Password</h1>

                        <form >
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
                                    <button class="button">Updatek</button>
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
import axios from 'axios';

export default {
    data() {
    return {
      password: '',
      password2: '',
      errors: [],
    };
  },

};
</script>