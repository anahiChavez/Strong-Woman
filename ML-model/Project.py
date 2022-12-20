{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "10054a18",
   "metadata": {
    "id": "10054a18"
   },
   "outputs": [],
   "source": [
    "# Libraries \n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "%matplotlib inline \n",
    "\n",
    "# Model\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# Model evaluatorrs\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "from sklearn.model_selection import RandomizedSearchCV, GridSearchCV\n",
    "from sklearn.metrics import confusion_matrix, classification_report\n",
    "from sklearn.metrics import precision_score, recall_score, f1_score\n",
    "from sklearn.metrics import plot_roc_curve"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e25f58d6",
   "metadata": {
    "id": "e25f58d6"
   },
   "source": [
    "## Data Exploration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5101e8bc",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5101e8bc",
    "outputId": "aa137320-2bfa-4cb2-efc0-7f2da7aeec03"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(569, 33)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"breast_cancer.csv\")\n",
    "df.shape # (rows, columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ea3f0114",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 317
    },
    "id": "ea3f0114",
    "outputId": "9365f7c3-6d13-490a-f22a-43ea5552297d"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>radius_mean</th>\n",
       "      <th>texture_mean</th>\n",
       "      <th>perimeter_mean</th>\n",
       "      <th>area_mean</th>\n",
       "      <th>smoothness_mean</th>\n",
       "      <th>compactness_mean</th>\n",
       "      <th>concavity_mean</th>\n",
       "      <th>concave points_mean</th>\n",
       "      <th>...</th>\n",
       "      <th>texture_worst</th>\n",
       "      <th>perimeter_worst</th>\n",
       "      <th>area_worst</th>\n",
       "      <th>smoothness_worst</th>\n",
       "      <th>compactness_worst</th>\n",
       "      <th>concavity_worst</th>\n",
       "      <th>concave points_worst</th>\n",
       "      <th>symmetry_worst</th>\n",
       "      <th>fractal_dimension_worst</th>\n",
       "      <th>Unnamed: 32</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842302</td>\n",
       "      <td>M</td>\n",
       "      <td>17.99</td>\n",
       "      <td>10.38</td>\n",
       "      <td>122.80</td>\n",
       "      <td>1001.0</td>\n",
       "      <td>0.11840</td>\n",
       "      <td>0.27760</td>\n",
       "      <td>0.3001</td>\n",
       "      <td>0.14710</td>\n",
       "      <td>...</td>\n",
       "      <td>17.33</td>\n",
       "      <td>184.60</td>\n",
       "      <td>2019.0</td>\n",
       "      <td>0.1622</td>\n",
       "      <td>0.6656</td>\n",
       "      <td>0.7119</td>\n",
       "      <td>0.2654</td>\n",
       "      <td>0.4601</td>\n",
       "      <td>0.11890</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>842517</td>\n",
       "      <td>M</td>\n",
       "      <td>20.57</td>\n",
       "      <td>17.77</td>\n",
       "      <td>132.90</td>\n",
       "      <td>1326.0</td>\n",
       "      <td>0.08474</td>\n",
       "      <td>0.07864</td>\n",
       "      <td>0.0869</td>\n",
       "      <td>0.07017</td>\n",
       "      <td>...</td>\n",
       "      <td>23.41</td>\n",
       "      <td>158.80</td>\n",
       "      <td>1956.0</td>\n",
       "      <td>0.1238</td>\n",
       "      <td>0.1866</td>\n",
       "      <td>0.2416</td>\n",
       "      <td>0.1860</td>\n",
       "      <td>0.2750</td>\n",
       "      <td>0.08902</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>84300903</td>\n",
       "      <td>M</td>\n",
       "      <td>19.69</td>\n",
       "      <td>21.25</td>\n",
       "      <td>130.00</td>\n",
       "      <td>1203.0</td>\n",
       "      <td>0.10960</td>\n",
       "      <td>0.15990</td>\n",
       "      <td>0.1974</td>\n",
       "      <td>0.12790</td>\n",
       "      <td>...</td>\n",
       "      <td>25.53</td>\n",
       "      <td>152.50</td>\n",
       "      <td>1709.0</td>\n",
       "      <td>0.1444</td>\n",
       "      <td>0.4245</td>\n",
       "      <td>0.4504</td>\n",
       "      <td>0.2430</td>\n",
       "      <td>0.3613</td>\n",
       "      <td>0.08758</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>84348301</td>\n",
       "      <td>M</td>\n",
       "      <td>11.42</td>\n",
       "      <td>20.38</td>\n",
       "      <td>77.58</td>\n",
       "      <td>386.1</td>\n",
       "      <td>0.14250</td>\n",
       "      <td>0.28390</td>\n",
       "      <td>0.2414</td>\n",
       "      <td>0.10520</td>\n",
       "      <td>...</td>\n",
       "      <td>26.50</td>\n",
       "      <td>98.87</td>\n",
       "      <td>567.7</td>\n",
       "      <td>0.2098</td>\n",
       "      <td>0.8663</td>\n",
       "      <td>0.6869</td>\n",
       "      <td>0.2575</td>\n",
       "      <td>0.6638</td>\n",
       "      <td>0.17300</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>84358402</td>\n",
       "      <td>M</td>\n",
       "      <td>20.29</td>\n",
       "      <td>14.34</td>\n",
       "      <td>135.10</td>\n",
       "      <td>1297.0</td>\n",
       "      <td>0.10030</td>\n",
       "      <td>0.13280</td>\n",
       "      <td>0.1980</td>\n",
       "      <td>0.10430</td>\n",
       "      <td>...</td>\n",
       "      <td>16.67</td>\n",
       "      <td>152.20</td>\n",
       "      <td>1575.0</td>\n",
       "      <td>0.1374</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.4000</td>\n",
       "      <td>0.1625</td>\n",
       "      <td>0.2364</td>\n",
       "      <td>0.07678</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         id diagnosis  radius_mean  texture_mean  perimeter_mean  area_mean  \\\n",
       "0    842302         M        17.99         10.38          122.80     1001.0   \n",
       "1    842517         M        20.57         17.77          132.90     1326.0   \n",
       "2  84300903         M        19.69         21.25          130.00     1203.0   \n",
       "3  84348301         M        11.42         20.38           77.58      386.1   \n",
       "4  84358402         M        20.29         14.34          135.10     1297.0   \n",
       "\n",
       "   smoothness_mean  compactness_mean  concavity_mean  concave points_mean  \\\n",
       "0          0.11840           0.27760          0.3001              0.14710   \n",
       "1          0.08474           0.07864          0.0869              0.07017   \n",
       "2          0.10960           0.15990          0.1974              0.12790   \n",
       "3          0.14250           0.28390          0.2414              0.10520   \n",
       "4          0.10030           0.13280          0.1980              0.10430   \n",
       "\n",
       "   ...  texture_worst  perimeter_worst  area_worst  smoothness_worst  \\\n",
       "0  ...          17.33           184.60      2019.0            0.1622   \n",
       "1  ...          23.41           158.80      1956.0            0.1238   \n",
       "2  ...          25.53           152.50      1709.0            0.1444   \n",
       "3  ...          26.50            98.87       567.7            0.2098   \n",
       "4  ...          16.67           152.20      1575.0            0.1374   \n",
       "\n",
       "   compactness_worst  concavity_worst  concave points_worst  symmetry_worst  \\\n",
       "0             0.6656           0.7119                0.2654          0.4601   \n",
       "1             0.1866           0.2416                0.1860          0.2750   \n",
       "2             0.4245           0.4504                0.2430          0.3613   \n",
       "3             0.8663           0.6869                0.2575          0.6638   \n",
       "4             0.2050           0.4000                0.1625          0.2364   \n",
       "\n",
       "   fractal_dimension_worst  Unnamed: 32  \n",
       "0                  0.11890          NaN  \n",
       "1                  0.08902          NaN  \n",
       "2                  0.08758          NaN  \n",
       "3                  0.17300          NaN  \n",
       "4                  0.07678          NaN  \n",
       "\n",
       "[5 rows x 33 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# View top 5 rows of the dataframe\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "548d81d2",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "548d81d2",
    "outputId": "2e53b36e-cc1b-4b51-8482-16212ce46f3f"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "B    357\n",
       "M    212\n",
       "Name: diagnosis, dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# See the postivies (B) and negatives (M) samples\n",
    "df.diagnosis.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "718761bb",
   "metadata": {
    "id": "718761bb"
   },
   "outputs": [],
   "source": [
    "#Getting DataFrame ready\n",
    "df.replace({'M':1, 'B':0}, inplace=True)\n",
    "breast_dataFrame = df.iloc[:, 12:22]\n",
    "breast_dataFrame['diagnosis'] = df['diagnosis']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f21a72fd",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 505
    },
    "id": "f21a72fd",
    "outputId": "78d8cad7-139d-4d4a-a9af-6ea080411e5b"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>radius_se</th>\n",
       "      <th>texture_se</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>area_se</th>\n",
       "      <th>smoothness_se</th>\n",
       "      <th>compactness_se</th>\n",
       "      <th>concavity_se</th>\n",
       "      <th>concave points_se</th>\n",
       "      <th>symmetry_se</th>\n",
       "      <th>fractal_dimension_se</th>\n",
       "      <th>diagnosis</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0950</td>\n",
       "      <td>0.9053</td>\n",
       "      <td>8.589</td>\n",
       "      <td>153.40</td>\n",
       "      <td>0.006399</td>\n",
       "      <td>0.04904</td>\n",
       "      <td>0.05373</td>\n",
       "      <td>0.015870</td>\n",
       "      <td>0.03003</td>\n",
       "      <td>0.006193</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.5435</td>\n",
       "      <td>0.7339</td>\n",
       "      <td>3.398</td>\n",
       "      <td>74.08</td>\n",
       "      <td>0.005225</td>\n",
       "      <td>0.01308</td>\n",
       "      <td>0.01860</td>\n",
       "      <td>0.013400</td>\n",
       "      <td>0.01389</td>\n",
       "      <td>0.003532</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.7456</td>\n",
       "      <td>0.7869</td>\n",
       "      <td>4.585</td>\n",
       "      <td>94.03</td>\n",
       "      <td>0.006150</td>\n",
       "      <td>0.04006</td>\n",
       "      <td>0.03832</td>\n",
       "      <td>0.020580</td>\n",
       "      <td>0.02250</td>\n",
       "      <td>0.004571</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.4956</td>\n",
       "      <td>1.1560</td>\n",
       "      <td>3.445</td>\n",
       "      <td>27.23</td>\n",
       "      <td>0.009110</td>\n",
       "      <td>0.07458</td>\n",
       "      <td>0.05661</td>\n",
       "      <td>0.018670</td>\n",
       "      <td>0.05963</td>\n",
       "      <td>0.009208</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.7572</td>\n",
       "      <td>0.7813</td>\n",
       "      <td>5.438</td>\n",
       "      <td>94.44</td>\n",
       "      <td>0.011490</td>\n",
       "      <td>0.02461</td>\n",
       "      <td>0.05688</td>\n",
       "      <td>0.018850</td>\n",
       "      <td>0.01756</td>\n",
       "      <td>0.005115</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75</th>\n",
       "      <td>0.7474</td>\n",
       "      <td>1.0160</td>\n",
       "      <td>5.029</td>\n",
       "      <td>79.25</td>\n",
       "      <td>0.010820</td>\n",
       "      <td>0.02203</td>\n",
       "      <td>0.03500</td>\n",
       "      <td>0.018090</td>\n",
       "      <td>0.01550</td>\n",
       "      <td>0.001948</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>76</th>\n",
       "      <td>0.4101</td>\n",
       "      <td>1.0140</td>\n",
       "      <td>2.652</td>\n",
       "      <td>32.65</td>\n",
       "      <td>0.013400</td>\n",
       "      <td>0.02839</td>\n",
       "      <td>0.01162</td>\n",
       "      <td>0.008239</td>\n",
       "      <td>0.02572</td>\n",
       "      <td>0.006164</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>77</th>\n",
       "      <td>0.9806</td>\n",
       "      <td>0.5505</td>\n",
       "      <td>6.311</td>\n",
       "      <td>134.80</td>\n",
       "      <td>0.007940</td>\n",
       "      <td>0.05839</td>\n",
       "      <td>0.04658</td>\n",
       "      <td>0.020700</td>\n",
       "      <td>0.02591</td>\n",
       "      <td>0.007054</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>78</th>\n",
       "      <td>0.9317</td>\n",
       "      <td>1.8850</td>\n",
       "      <td>8.649</td>\n",
       "      <td>116.40</td>\n",
       "      <td>0.010380</td>\n",
       "      <td>0.06835</td>\n",
       "      <td>0.10910</td>\n",
       "      <td>0.025930</td>\n",
       "      <td>0.07895</td>\n",
       "      <td>0.005987</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>79</th>\n",
       "      <td>0.2655</td>\n",
       "      <td>1.0950</td>\n",
       "      <td>1.778</td>\n",
       "      <td>20.35</td>\n",
       "      <td>0.005293</td>\n",
       "      <td>0.01661</td>\n",
       "      <td>0.02071</td>\n",
       "      <td>0.008179</td>\n",
       "      <td>0.01748</td>\n",
       "      <td>0.002848</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>80 rows × 11 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    radius_se  texture_se  perimeter_se  area_se  smoothness_se  \\\n",
       "0      1.0950      0.9053         8.589   153.40       0.006399   \n",
       "1      0.5435      0.7339         3.398    74.08       0.005225   \n",
       "2      0.7456      0.7869         4.585    94.03       0.006150   \n",
       "3      0.4956      1.1560         3.445    27.23       0.009110   \n",
       "4      0.7572      0.7813         5.438    94.44       0.011490   \n",
       "..        ...         ...           ...      ...            ...   \n",
       "75     0.7474      1.0160         5.029    79.25       0.010820   \n",
       "76     0.4101      1.0140         2.652    32.65       0.013400   \n",
       "77     0.9806      0.5505         6.311   134.80       0.007940   \n",
       "78     0.9317      1.8850         8.649   116.40       0.010380   \n",
       "79     0.2655      1.0950         1.778    20.35       0.005293   \n",
       "\n",
       "    compactness_se  concavity_se  concave points_se  symmetry_se  \\\n",
       "0          0.04904       0.05373           0.015870      0.03003   \n",
       "1          0.01308       0.01860           0.013400      0.01389   \n",
       "2          0.04006       0.03832           0.020580      0.02250   \n",
       "3          0.07458       0.05661           0.018670      0.05963   \n",
       "4          0.02461       0.05688           0.018850      0.01756   \n",
       "..             ...           ...                ...          ...   \n",
       "75         0.02203       0.03500           0.018090      0.01550   \n",
       "76         0.02839       0.01162           0.008239      0.02572   \n",
       "77         0.05839       0.04658           0.020700      0.02591   \n",
       "78         0.06835       0.10910           0.025930      0.07895   \n",
       "79         0.01661       0.02071           0.008179      0.01748   \n",
       "\n",
       "    fractal_dimension_se  diagnosis  \n",
       "0               0.006193          1  \n",
       "1               0.003532          1  \n",
       "2               0.004571          1  \n",
       "3               0.009208          1  \n",
       "4               0.005115          1  \n",
       "..                   ...        ...  \n",
       "75              0.001948          1  \n",
       "76              0.006164          0  \n",
       "77              0.007054          1  \n",
       "78              0.005987          1  \n",
       "79              0.002848          0  \n",
       "\n",
       "[80 rows x 11 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "breast_dataFrame[:80]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "66655b66",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "66655b66",
    "outputId": "7627a642-9737-4acc-da61-bee347458233",
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "radius_se               float64\n",
       "texture_se              float64\n",
       "perimeter_se            float64\n",
       "area_se                 float64\n",
       "smoothness_se           float64\n",
       "compactness_se          float64\n",
       "concavity_se            float64\n",
       "concave points_se       float64\n",
       "symmetry_se             float64\n",
       "fractal_dimension_se    float64\n",
       "diagnosis                 int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "breast_dataFrame.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "kVkolLpc206A",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 193
    },
    "id": "kVkolLpc206A",
    "outputId": "7b6dbd35-8459-46f8-d7eb-f2a5e9ec4114"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>radius_se</th>\n",
       "      <th>texture_se</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>area_se</th>\n",
       "      <th>smoothness_se</th>\n",
       "      <th>compactness_se</th>\n",
       "      <th>concavity_se</th>\n",
       "      <th>concave points_se</th>\n",
       "      <th>symmetry_se</th>\n",
       "      <th>fractal_dimension_se</th>\n",
       "      <th>diagnosis</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0950</td>\n",
       "      <td>0.9053</td>\n",
       "      <td>8.589</td>\n",
       "      <td>153.40</td>\n",
       "      <td>0.006399</td>\n",
       "      <td>0.04904</td>\n",
       "      <td>0.05373</td>\n",
       "      <td>0.01587</td>\n",
       "      <td>0.03003</td>\n",
       "      <td>0.006193</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.5435</td>\n",
       "      <td>0.7339</td>\n",
       "      <td>3.398</td>\n",
       "      <td>74.08</td>\n",
       "      <td>0.005225</td>\n",
       "      <td>0.01308</td>\n",
       "      <td>0.01860</td>\n",
       "      <td>0.01340</td>\n",
       "      <td>0.01389</td>\n",
       "      <td>0.003532</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   radius_se  texture_se  perimeter_se  area_se  smoothness_se  \\\n",
       "0     1.0950      0.9053         8.589   153.40       0.006399   \n",
       "1     0.5435      0.7339         3.398    74.08       0.005225   \n",
       "\n",
       "   compactness_se  concavity_se  concave points_se  symmetry_se  \\\n",
       "0         0.04904       0.05373            0.01587      0.03003   \n",
       "1         0.01308       0.01860            0.01340      0.01389   \n",
       "\n",
       "   fractal_dimension_se  diagnosis  \n",
       "0              0.006193          1  \n",
       "1              0.003532          1  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "breast_dataFrame[:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "88721d66",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 295
    },
    "id": "88721d66",
    "outputId": "430a2a56-af51-4f1e-e37a-bff90305a0ee"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot the values counts with a bar graph\n",
    "breast_dataFrame.diagnosis.value_counts().plot(kind='bar', color=['salmon', 'lightblue'])\n",
    "plt.title('Breast Cancer Diagnosis')\n",
    "plt.ylabel('Number of Patients')\n",
    "plt.xlabel('0 = No Disease  -   1 = Disease')\n",
    "plt.ylabel(\"Amount\")\n",
    "plt.xticks(rotation=0);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "30586db8",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "30586db8",
    "outputId": "05bc5931-a58d-4ff3-ff06-ab6304cfd20a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 569 entries, 0 to 568\n",
      "Data columns (total 11 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   radius_se             569 non-null    float64\n",
      " 1   texture_se            569 non-null    float64\n",
      " 2   perimeter_se          569 non-null    float64\n",
      " 3   area_se               569 non-null    float64\n",
      " 4   smoothness_se         569 non-null    float64\n",
      " 5   compactness_se        569 non-null    float64\n",
      " 6   concavity_se          569 non-null    float64\n",
      " 7   concave points_se     569 non-null    float64\n",
      " 8   symmetry_se           569 non-null    float64\n",
      " 9   fractal_dimension_se  569 non-null    float64\n",
      " 10  diagnosis             569 non-null    int64  \n",
      "dtypes: float64(10), int64(1)\n",
      "memory usage: 49.0 KB\n"
     ]
    }
   ],
   "source": [
    "breast_dataFrame.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c1f95bc0",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "c1f95bc0",
    "outputId": "bea532d2-e2f8-47ae-b9f5-75aeafd04d0d"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x2548b225d80>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1855.5x1800 with 110 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a pair plot\n",
    "sns.pairplot(breast_dataFrame, hue='diagnosis')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "170c9ab7",
   "metadata": {
    "id": "170c9ab7"
   },
   "source": [
    "## Modeling"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "829afdb5",
   "metadata": {
    "id": "829afdb5"
   },
   "source": [
    "### Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8cf16f0e",
   "metadata": {
    "id": "8cf16f0e"
   },
   "outputs": [],
   "source": [
    "# Create X (all the feature columns)\n",
    "X = breast_dataFrame.drop('diagnosis', axis=1)\n",
    "\n",
    "# Create y (the target column)\n",
    "y =  breast_dataFrame['diagnosis']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "3fd19ec2",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 267
    },
    "id": "3fd19ec2",
    "outputId": "665f7fef-cc10-48f1-99c0-0c2b3b18c82d"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>radius_se</th>\n",
       "      <th>texture_se</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>area_se</th>\n",
       "      <th>smoothness_se</th>\n",
       "      <th>compactness_se</th>\n",
       "      <th>concavity_se</th>\n",
       "      <th>concave points_se</th>\n",
       "      <th>symmetry_se</th>\n",
       "      <th>fractal_dimension_se</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.0950</td>\n",
       "      <td>0.9053</td>\n",
       "      <td>8.589</td>\n",
       "      <td>153.40</td>\n",
       "      <td>0.006399</td>\n",
       "      <td>0.04904</td>\n",
       "      <td>0.05373</td>\n",
       "      <td>0.01587</td>\n",
       "      <td>0.03003</td>\n",
       "      <td>0.006193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.5435</td>\n",
       "      <td>0.7339</td>\n",
       "      <td>3.398</td>\n",
       "      <td>74.08</td>\n",
       "      <td>0.005225</td>\n",
       "      <td>0.01308</td>\n",
       "      <td>0.01860</td>\n",
       "      <td>0.01340</td>\n",
       "      <td>0.01389</td>\n",
       "      <td>0.003532</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.7456</td>\n",
       "      <td>0.7869</td>\n",
       "      <td>4.585</td>\n",
       "      <td>94.03</td>\n",
       "      <td>0.006150</td>\n",
       "      <td>0.04006</td>\n",
       "      <td>0.03832</td>\n",
       "      <td>0.02058</td>\n",
       "      <td>0.02250</td>\n",
       "      <td>0.004571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.4956</td>\n",
       "      <td>1.1560</td>\n",
       "      <td>3.445</td>\n",
       "      <td>27.23</td>\n",
       "      <td>0.009110</td>\n",
       "      <td>0.07458</td>\n",
       "      <td>0.05661</td>\n",
       "      <td>0.01867</td>\n",
       "      <td>0.05963</td>\n",
       "      <td>0.009208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.7572</td>\n",
       "      <td>0.7813</td>\n",
       "      <td>5.438</td>\n",
       "      <td>94.44</td>\n",
       "      <td>0.011490</td>\n",
       "      <td>0.02461</td>\n",
       "      <td>0.05688</td>\n",
       "      <td>0.01885</td>\n",
       "      <td>0.01756</td>\n",
       "      <td>0.005115</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   radius_se  texture_se  perimeter_se  area_se  smoothness_se  \\\n",
       "0     1.0950      0.9053         8.589   153.40       0.006399   \n",
       "1     0.5435      0.7339         3.398    74.08       0.005225   \n",
       "2     0.7456      0.7869         4.585    94.03       0.006150   \n",
       "3     0.4956      1.1560         3.445    27.23       0.009110   \n",
       "4     0.7572      0.7813         5.438    94.44       0.011490   \n",
       "\n",
       "   compactness_se  concavity_se  concave points_se  symmetry_se  \\\n",
       "0         0.04904       0.05373            0.01587      0.03003   \n",
       "1         0.01308       0.01860            0.01340      0.01389   \n",
       "2         0.04006       0.03832            0.02058      0.02250   \n",
       "3         0.07458       0.05661            0.01867      0.05963   \n",
       "4         0.02461       0.05688            0.01885      0.01756   \n",
       "\n",
       "   fractal_dimension_se  \n",
       "0              0.006193  \n",
       "1              0.003532  \n",
       "2              0.004571  \n",
       "3              0.009208  \n",
       "4              0.005115  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c5395c02",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "c5395c02",
    "outputId": "dbf12d3b-7e65-4864-9591-ed2cddd45f33"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0    1\n",
       " 1    1\n",
       " 2    1\n",
       " 3    1\n",
       " 4    1\n",
       " Name: diagnosis, dtype: int64,\n",
       " 0    357\n",
       " 1    212\n",
       " Name: diagnosis, dtype: int64)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y.head(), y.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2642a14a",
   "metadata": {
    "id": "2642a14a"
   },
   "outputs": [],
   "source": [
    "# Random seed for reproducibility\n",
    "np.random.seed(42)\n",
    "\n",
    "# Split into train & test set\n",
    "X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a87013aa",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "a87013aa",
    "outputId": "e132c703-de7c-43ca-8347-0f37681dfd30"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(455, 114)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(y_train), len(y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d49b1b55",
   "metadata": {
    "id": "d49b1b55"
   },
   "source": [
    "### Hyperparameter tuning 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "03175003",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "03175003",
    "outputId": "e0ed58fd-57da-44db-b015-b993b4e72c64"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9385964912280702"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# \n",
    "model = LogisticRegression()\n",
    "\n",
    "# Random seed for reproducible results\n",
    "np.random.seed(42)\n",
    "\n",
    "# Fit the model\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Evaluate the model a\n",
    "model.score(X_test, y_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "355c00ae",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 407
    },
    "id": "355c00ae",
    "outputId": "35bebd0d-cb77-42ea-a400-77f354c833fb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.93      0.97      0.95        71\n",
      "           1       0.95      0.88      0.92        43\n",
      "\n",
      "    accuracy                           0.94       114\n",
      "   macro avg       0.94      0.93      0.93       114\n",
      "weighted avg       0.94      0.94      0.94       114\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 216x216 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_preds = model.predict(X_test)\n",
    "sns.set(font_scale=1.5) # Increase font size\n",
    "\n",
    "def plot_conf_mat(y_test, y_preds):\n",
    "    \"\"\"\n",
    "    Plots a confusion matrix using Seaborn's heatmap().\n",
    "    \"\"\"\n",
    "    fig, ax = plt.subplots(figsize=(3, 3))\n",
    "    ax = sns.heatmap(confusion_matrix(y_test, y_preds),\n",
    "                     annot=True, # Annotate the boxes\n",
    "                     cbar=False)\n",
    "    plt.xlabel(\"true label\")\n",
    "    plt.ylabel(\"predicted label\")\n",
    "    \n",
    "plot_conf_mat(y_test, y_preds)\n",
    "\n",
    "print(classification_report(y_test, y_preds))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "314c3955",
   "metadata": {
    "id": "314c3955"
   },
   "outputs": [],
   "source": [
    "## Tuning models with with RandomizedSearchCV\n",
    "\n",
    "# Different LogisticRegression hyperparameters\n",
    "log_reg_grid = {\"C\": np.logspace(-4, 4, 20),\n",
    "                \"solver\": [\"liblinear\"]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b169566b",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "b169566b",
    "outputId": "9eedf2a5-ee22-4633-c08d-b87a5ef8aee0"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 5 folds for each of 20 candidates, totalling 100 fits\n"
     ]
    }
   ],
   "source": [
    "# Create X (all the feature columns)\n",
    "X = breast_dataFrame.drop('diagnosis', axis=1)\n",
    "\n",
    "# Create y (the target column)\n",
    "y =  breast_dataFrame['diagnosis']\n",
    "\n",
    "# Split into train & test set\n",
    "X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2)\n",
    "\n",
    "# Setup random seed\n",
    "np.random.seed(42)\n",
    "\n",
    "# Setup random hyperparameter search for LogisticRegression\n",
    "rs_log_reg = RandomizedSearchCV(LogisticRegression(),\n",
    "                                param_distributions=log_reg_grid,\n",
    "                                cv=5,\n",
    "                                n_iter=20,\n",
    "                                verbose=True)\n",
    "\n",
    "# Fit random hyperparameter search model\n",
    "rs_log_reg.fit(X_train, y_train);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "331b7d0c",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "331b7d0c",
    "outputId": "7c86afd5-c4c0-4cef-dd7d-5dd62b84b1e5"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9473684210526315"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rs_log_reg.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "HVwuVcYiBjKa",
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 407
    },
    "id": "HVwuVcYiBjKa",
    "outputId": "96ee2a5b-a10a-478c-f44e-6bebc9a32fa5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.93      0.99      0.96        71\n",
      "           1       0.97      0.88      0.93        43\n",
      "\n",
      "    accuracy                           0.95       114\n",
      "   macro avg       0.95      0.93      0.94       114\n",
      "weighted avg       0.95      0.95      0.95       114\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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6HQ69u7dq146IWqZUgvZrFmzYpNWNWvWrEoCCVGblesasjqQa0j1yDWkulSZMUAIUflKPWUdMWJEuXa4bt26cocRorYrtZBXr14tsSwjIwO9Xo+Liwve3t4YjUbS0tLIysrC1dVVU88hhaiOSi3kvn37in39448/MmbMGObOncuLL76IldXvZ7vx8fG8++67DB8+vPKSClELmH0N+be//Y2QkBBefvnlYmUEGDhwIOHh4URHR6seUIjaxOxCpqSk4OPjU+r6Jk2acOPGDTUyCVFrmV1IX19fduzYQVFRUYl1er2euLg4WrdurWo4IWobs4fOvfHGG7z99tuEh4czePBgPD090ev1XL58mU2bNpGens6KFSsqM6sQNZ7ZhQwODiY/P5+FCxcye/Zs06vLFUWhefPmLF26lICAgEoLKkRtUOaROkajkZ9//pm0tDR0Oh2enp60a9eusvKVm5ZH6uza9y86P9WpxPLtX33DayMmWCDRo2lppI591ydoMCECu9a+GHPzyN55gJufrEPJyzdtY9fej0ZTXqVe57YoRiN3j5zixrxVFCSnWTD571T9tIeVlRWNGjXCaDTSokUL7OzsMBqNJe68itK18m/J19v3EL9td7HlV1PTLZSoerDv0gnPf/6N/J8vcnPhGuo0bYDbiJeo27EVKeHTQFGw9W2OV8xclHw9tz7dCID7qMF4bVrA5RejMNzItPBv8WhlKuTx48f54IMPOHPmDACrV6+mqKiImTNnMn36dIKD5TXij+Pl3RxHJwd2fb2PuH9tt3ScaqXRO6MpTL9JyvB3UPT33iNTmH6TJnOicOjxFLnfH8Nt5MtYO9qTPHwa+jNJAOQdPolPXDRur7zMzfmrLfkrPJbZh7XExEReffVVcnNzGTlyJPfPdF1cXLCxsWHKlCkkJCRUWtCaonWbVgBcOCcTS5eFzrYOhszb3I7dZSojQN6RUwDYtfYBoI5nEwyZt01lBMg/dQFD1m3s/H2qMnK5lGleVg8PD7766iveeOMN0/KOHTuybds2WrZsKXdZzdC67b05bc+fv1dIe/t6loxTbSgFhVx9bRYZy/9VbHndtveubwvT770UqvBKOtYujli7/f6WNisXR6ydHDHcLH3WRK0wu5AnTpxg8ODB1K1b13SH9T5HR0eGDh3KhQsXVA9Y07Rp24rsOzn89cPpXLp6nORr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\n",
      "text/plain": [
       "<Figure size 216x216 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_preds = rs_log_reg.predict(X_test)\n",
    "sns.set(font_scale=1.5) # Increase font size\n",
    "\n",
    "plot_conf_mat(y_test, y_preds)\n",
    "\n",
    "print(classification_report(y_test, y_preds))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "7t3ZoGOZQDSZ",
   "metadata": {
    "id": "7t3ZoGOZQDSZ"
   },
   "outputs": [],
   "source": [
    "import pickle\n",
    "\n",
    "# Save the model to file\n",
    "pickle.dump(rs_log_reg, open(\"lr_breastCancer.pkl\", \"wb\"))"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}