<template>
  <div class="d-flex flex-column justify-content-center align-items-center" style="height: 80vh">
    <div class="p-2">
      <h1 v-if="!APIResult.length">Enter to predict Your Stats</h1>
      <h1 v-else style="font-size:4rem">{{APIResult}}</h1>
    </div>
    <div class="p-2">
        <form @submit.prevent>
            <div class="form-row" style="max-width:500px">
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="A">Age</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.A"
                    type="number"
                    id="A"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="B">Sex</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.B"
                    type="number"
                    id="B"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="C">Chest Pain</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.C"
                    type="number"
                    id="C"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="D">Trest BPS</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.D"
                    type="number"
                    id="D"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="E">Cholesterol</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.E"
                    type="number"
                    id="E"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="F">FBS</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.F"
                    type="number"
                    id="F"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="G">Resting ECG</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.G"
                    type="number"
                    id="G"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="H">Thalach</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.H"
                    type="number"
                    id="H"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="I">Exang</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.I"
                    type="number"
                    id="I"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="J">Old Peak</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.J"
                    type="number"
                    id="J"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="K">Slope</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.K"
                    type="number"
                    id="K"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="L">CA</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.L"
                    type="number"
                    id="L"
                    />
                </div>
                <div class="form-group col-md-3">
                    <label class="col-12 px-0" for="M">Thal</label>
                    <input
                    class="form-control"
                    v-model.trim="heartdata.M"
                    type="number"
                    id="M"
                    />
                </div>
                
            <button @click="predict" type="button" class="btn btn-primary btn-lg btn-block">Submit</button>
            </div>
        </form>
    </div>
  </div>
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