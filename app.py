{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a931291",
   "metadata": {},
   "outputs": [],
   "source": [
    "conda install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bec80229",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16a63d0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "21dbabf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c42ab5e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "from keras.models import load_model\n",
    "@app.route(\"/\",methods = [\"GET\",\"POST\"])\n",
    "def index():\n",
    "    \n",
    "    if request.method == \"POST\":\n",
    "        NPTA = request.form.get(\"NPTA\")\n",
    "        TLTA = request.form.get(\"TLTA\")\n",
    "        WCTA = request.form.get(\"WCTA\")\n",
    "        print(NPTA,TLTA,WCTA)\n",
    "        model = load_model(\"bankruptcy_model\")\n",
    "        pred = model.predict([[float(NPTA),float(TLTA),float(WCTA)]])\n",
    "        return (render_template(\"index.html\",result=pred))\n",
    "    else:\n",
    "        return (render_template(\"index.html\",result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1adf57b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2efa1dd6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc5911ae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed36b7e7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
