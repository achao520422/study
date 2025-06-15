import {defineStore} from "pinia";

export const useAuthStore  = defineStore('user', {
    state: () => ({ auth: false}),
    getters: {
        isAuthenticated: (state) => !!state.auth,
    },
    actions: {
        needAuth() {
            this.auth = true;
        },
        disableAuth() {
            this.auth = false;
        }
    },
})