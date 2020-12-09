<template>
    <h1>Hi</h1>
</template>

<script>
console.log('ere')
import { getAPI } from "@/axios";
export default {
    name: "Posts",
    data() {
        return {
            heartdata: {
                A: "",
                B: "",
                C: "",
                D: "",
                E: "",
                F: "",
                G: "",
                H: "",
                I: "",
                J: "",
                K: "",
                L: "",
                M: ""
            },
            APIResult: []
        };
    },
    methods: {
        predict(){
            getAPI
            .get("/posts", {
                params: {
                    A: this.heartdata.A,
                    B: this.heartdata.B,
                    C: this.heartdata.C,
                    D: this.heartdata.D,
                    E: this.heartdata.E,
                    F: this.heartdata.F,
                    G: this.heartdata.G,
                    H: this.heartdata.H,
                    I: this.heartdata.I,
                    J: this.heartdata.K,
                    L: this.heartdata.L,
                    M: this.heartdata.M
                }
            })
            .then(response => {
                console.log("Received data successfully");
                this.APIResult = response.data;
                console.log(response.data);
            })
            .catch(err => {
                console.log(err);
            });
        }
    }
 };
</script>