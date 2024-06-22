<template>
  <v-row 
    no-gutters 
    class="mb-8 px-16"
  >
    <v-col 
      xs="0" 
      sm="0" 
      md="0" 
      lg="1" 
      xl="1"
    >
    </v-col>

    <v-col 
      xs="12" 
      sm="12" 
      md="12" 
      lg="10" 
      xl="10" 
      class="pt-8"
    >
      <div v-if="receiptData">
        <div class="text-h3 font-weight-normal mb-5 text-center">
          <span id="span">{{ receiptData.name }}</span>
        </div>
        <v-img 
          style="height: 450px;" 
          :src="receiptData.image" 
          cover 
          class="my-auto"
        >
        </v-img>

        <div class="text-h6 mt-4 mb-2 text-center">
          <span id="span">{{ receiptData.description }}</span>
        </div>

        <v-divider class="my-8"></v-divider>

        <div class="d-flex">
          <div>
            <div class="text-h5 font-weight-bold ml-2">
              <span id="span">Ingredientes</span>
            </div>

            <v-row no-gutters>
              <v-col
                v-for="key in parsedIngredients" 
                :key="key"
                cols="5"
                md="6"
              >
                <div 
                  class="d-flex"
                >
                  <v-icon 
                    size="x-large" 
                    style="width: 12px; 
                    height: 12px;"
                    class="align-self-center"
                  >
                    mdi-circle-small
                  </v-icon>
      
                  <div class="text-h6">
                    <span id="span">{{ key }}</span>
                  </div>
                </div>
              </v-col>
            </v-row>
            </div>
            
            <v-spacer></v-spacer>
            <div>
              <div class="text-h5 font-weight-bold ml-2">
                <span id="span">Classificação Média:</span>
              </div>
              <v-rating
                v-model="receiptData.rate"
                readonly
              ></v-rating>
            </div>
          </div>

          <v-divider class="my-8"></v-divider>

          <div class="d-flex">
            <div class="d-flex">
              <div class="text-h6">
                <span id="span">Tempo de preparo:</span>
              </div>
              <div class="ml-2 text-h6 font-weight-bold">
                <span id="span">{{ receiptData.time }}</span>
              </div>
            </div>
            <div class="d-flex ml-4">
              <div class="text-h6">
                <span id="span">Serve:</span>
              </div>
              <div class="ml-2 text-h6 font-weight-bold">
                <span id="span">{{ receiptData.serve }}</span>
              </div>
            </div>
          </div>
          
        <v-divider class="my-8"><span class="font-weight-bold text-h5" id="span">Modo de preparo</span></v-divider>

        <div
          v-for="(key, index) in parsedPreparation"
          :key="key"
          class="d-flex"
        >
          <div class="ml-2 text-h6 font-weight-bold mb-4">
            <span id="span">{{ index + '.' }}</span>
          </div>
          <div class="ml-2 text-h6 font-weight-normal mb-4">
            <span id="span">{{ key }}</span>
          </div>
        </div>
      </div>

      <div v-if="receiptData">
        <div class="text-h5 font-weight-bold mt-8">
          <span id="span">Seção de comentários:</span>
        </div>
        <div>
          <div v-if="receiptData.comments == 0">
            <div class="text-h6 font-weight-normal mt-2">
              <span id="span">Ainda não há comentários, porque não escreve algum?</span>
            </div>
          </div>
          <div v-if="receiptData">
            <div
              v-for="(key, index) in receiptData.comments"
              :key="key.id"
              class="d-flex"
              >
              <div class="border-md w-100 mt-2 rounded-lg">
                <div class="text-subtitle-1 font-weight-normal ml-2 mt-2">
                  <span id="span">{{ key.name }}</span>
                </div>
                <div class="text-h6 font-weight-normal ml-4 mb-2">
                  <span id="span">{{ key.comment }}</span>
                </div>
              </div>
            </div>
          </div>

        </div>
        <v-sheet class="my-8" >
          <v-form 
            fast-fail 
            @submit.prevent="submitComment"
          >
            <v-text-field
              v-model="newComment.name"
              label="Nome"
            ></v-text-field>

            <v-text-field
              v-model="newComment.comment"
              label="Comentário"
            ></v-text-field>

            <v-btn class="mt-2" type="submit" block>Enviar Comentário</v-btn>
          </v-form>
        </v-sheet>
      </div>
    </v-col>

    <v-col 
      xs="0" 
      sm="0" 
      md="0" 
      lg="1" 
      xl="1"
    >
    </v-col>
  </v-row>
</template>
  
<script>
import axios from 'axios';
import { fetchCategories, getCategoryFromUrl, getRecipeFromUrl} from '@/utils.js'

export default {
  data() {
    return {
      receiptData: null,
      nameRules: [
        value => {
          if (value?.length >= 3) return true
          
          return 'Name must be at least 3 characters.'
        },
      ],
      commentRules: [
        value => {
          if (value?.length >= 5) return true

          return 'Comment must be at least 5 characters.'
        },
      ],
      recipes: [],
      filteredCategory: [],
      filteredRecipe: [],
      newComment: {
        name: '',
        comment: '',
      }
    }
  },
  computed: {
    parsedIngredients() {
      if (!this.receiptData) return [];
      return this.receiptData.ingredients.split('",\r\n"').map(item => item.replace(/(^"|"$)/g, ''));
    },
    parsedPreparation() {
      if (!this.receiptData) return [];
      return JSON.parse('{' + this.receiptData.preparation + '}');
    }
  },
  methods: {
    submitComment() {
      if (this.newComment.name.length >= 3 && this.newComment.comment.length >= 5) {
        const payload = {
          name: this.newComment.name,
          comment: this.newComment.comment,
          recipe: this.receiptData.id
        }
        axios
          .post(`http://127.0.0.1:8000/api/v1/recipes/${this.receiptData.id}/comments/`, payload)
          .then(response => {
            this.receiptData.comments.push(response.data);
            this.newComment.name = '';
            this.newComment.comment = '';
          })
          .catch(error => {
            console.error('Erro ao enviar comentário:', error);
          });
      }
    },
    fetchCategories(); 

    getCategoryFromUrl();

    getRecipeFromUrl() ;

    
    filterCategory() {
      const categoryName = this.getCategoryFromUrl();
      this.filteredCategory = this.recipes.find(recipe => recipe.name === categoryName);
    },
    filterRecipe() {
      const recipeName = this.getRecipeFromUrl();
      if (this.filteredCategory && Array.isArray(this.filteredCategory.recipes)) {
        this.filteredRecipe = this.filteredCategory.recipes.find(recipe => recipe.name === recipeName);
      }
    },
    finishData() {
      this.filterCategory();
      this.filterRecipe();
      if (this.filteredRecipe) {
        this.receiptData = this.filteredRecipe;
      }
    },
  },
  mounted() {
    this.fetchCategories();
  }
}
</script>
  
<style scoped>
#span{
  font-family: 'MyFont';
}
</style>