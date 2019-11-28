{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Funções"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "São usadas para executar blocos de códigos separados, chamados de escopo local.\n",
    "\n",
    "* Melhora na reusabilidade de código.\n",
    "* Decomposição procedural\n",
    "\n",
    "\n",
    "```\n",
    "def <name> (arg1, arg2,..., argN):\n",
    "    <statements>\n",
    "    \n",
    "    \n",
    "def <name> (arg1, arg2,..., argN):\n",
    "    <statements>\n",
    "    return <value>\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "'Valor somado 3'\n",
      "140055909295648\n",
      "140055909295648\n",
      "<function soma at 0x7f614eb8e620>\n",
      "<function soma at 0x7f614eb8e620>\n",
      "6\n",
      "140055909295648\n",
      "140055909297416\n",
      "\n",
      "novos valores\n",
      "140055909297416\n",
      "140055909297416\n"
     ]
    }
   ],
   "source": [
    "from pprint import pprint\n",
    "## Definindo uma função que  irá somar dois numeros inteiros\n",
    "\n",
    "def soma(n2, n1):\n",
    "    valor = n2 + n1\n",
    "    return valor\n",
    "\n",
    "# Para invocar essa função ela precisa ser chamada\n",
    "# E iremos armazenar o valor da soma que foi retornado\n",
    "valor_retornado_da_funcao = soma(1, 2)\n",
    "\n",
    "pprint(f\"Valor somado {valor_retornado_da_funcao}\")\n",
    "\n",
    "# Mas também podemos armazenar a função e não chamar pela\n",
    "guardando_a_referencia_para_funcao = soma\n",
    "\n",
    "pprint(id(guardando_a_referencia_para_funcao))\n",
    "pprint(id(soma))\n",
    "\n",
    "pprint(guardando_a_referencia_para_funcao)\n",
    "pprint(soma)\n",
    "\n",
    "# Invotando a funcao\n",
    "## Alguma lógica\n",
    "if False:\n",
    "    pprint(\"Não entra aqui\")\n",
    "else:\n",
    "    resultado = guardando_a_referencia_para_funcao(2, 4)\n",
    "    pprint(resultado)\n",
    "\n",
    "\n",
    "## Cuidao com redeclarações de funções e utilizar valores antigos..    \n",
    "def soma(n2, n1):\n",
    "    return n2 + n1 + 1\n",
    "\n",
    "pprint(id(guardando_a_referencia_para_funcao))\n",
    "pprint(id(soma))\n",
    "\n",
    "\n",
    "guardando_a_referencia_para_funcao = soma\n",
    "\n",
    "print(\"\\nnovos valores\")\n",
    "pprint(id(guardando_a_referencia_para_funcao))\n",
    "pprint(id(soma))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[0;31mSignature:\u001b[0m \u001b[0msoma\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum_1\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mSource:\u001b[0m   \n",
       "\u001b[0;32mdef\u001b[0m \u001b[0msoma\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum_1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mint\u001b[0m \u001b[0;34m,\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\n",
       "\u001b[0;34m\u001b[0m    \u001b[0;34m\"\"\"Soma dois numero inteiros\u001b[0m\n",
       "\u001b[0;34m    :args:\u001b[0m\n",
       "\u001b[0;34m        num_1: Objeto somável\u001b[0m\n",
       "\u001b[0;34m        num_2: Objeto somável\u001b[0m\n",
       "\u001b[0;34m    Retruns: soma de dois somáveis\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\n",
       "\u001b[0;34m\u001b[0m    \u001b[0;32mreturn\u001b[0m \u001b[0mnum_1\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mFile:\u001b[0m      ~/Files/mentorias-matheus/bora-ensinar-python/writing-not-complete/<ipython-input-3-4b373180d281>\n",
       "\u001b[0;31mType:\u001b[0m      function\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# P\n",
    "def soma(num_1:int , num_2:int) -> int:\n",
    "    \"\"\"Soma dois numero inteiros\n",
    "    :args:\n",
    "        num_1: Objeto somável\n",
    "        num_2: Objeto somável\n",
    "    Retruns: soma de dois somáveis\"\"\"\n",
    "    return num_1 + num_2\n",
    "\n",
    "soma??\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[0;31mSignature:\u001b[0m \u001b[0msoma\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum_1\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mSource:\u001b[0m   \n",
       "\u001b[0;32mdef\u001b[0m \u001b[0msoma\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnum_1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mint\u001b[0m \u001b[0;34m,\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mint\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\n",
       "\u001b[0;34m\u001b[0m    \u001b[0;34m\"\"\"Soma dois numero inteiros\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\n",
       "\u001b[0;34m\u001b[0m    \u001b[0;32mreturn\u001b[0m \u001b[0mnum_1\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mnum_2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mFile:\u001b[0m      ~/Files/mentorias-matheus/mentoria-gupy-codigos/<ipython-input-1-ff4bfb89732a>\n",
       "\u001b[0;31mType:\u001b[0m      function\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "soma??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[0;31mSignature:\u001b[0m \u001b[0msum\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0miterable\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstart\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m/\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
       "\u001b[0;31mDocstring:\u001b[0m\n",
       "Return the sum of a 'start' value (default: 0) plus an iterable of numbers\n",
       "\n",
       "When the iterable is empty, return the start value.\n",
       "This function is intended specifically for use with numeric values and may\n",
       "reject non-numeric types.\n",
       "\u001b[0;31mType:\u001b[0m      builtin_function_or_method\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sum??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def maximo(valor1, valor2, valor3):\n",
    "    maximo = valor1\n",
    "    if valor2 > maximo:\n",
    "        maximo = valor2\n",
    "    if valor3 > maximo:\n",
    "        maximo = valor3\n",
    "    return maximo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "31"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maximo(31,4,20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Parametros de funções\n",
    "# Funcoes nomeadas\n",
    "## Falta implementar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 (2, 3) {'x': 1, 'y': 2}\n"
     ]
    }
   ],
   "source": [
    "## Chamando o argumento da função pelo nome.\n",
    "\n",
    "## Argumento sem valore defatult\n",
    "def func(valor): pass\n",
    "def func1(valor1, valor): pass\n",
    "func1(valor='teste', valor1='teste2')\n",
    "\n",
    "## Argumentos com valor default\n",
    "def func2(valor='default'): pass\n",
    "\n",
    "## Argumentos não nomeados.. (*args)\n",
    "def func3(arg, arg2, agr3, *args): pass\n",
    "\n",
    "## Argumentos nomeados (**kwargs)\n",
    "def func4(arg, arg2, **kwargs): pass\n",
    "\n",
    "\n",
    "def func5(a, *args, **kwargs): print(a, args, kwargs)\n",
    "func5(1, 2, 3, x=1, y=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "aa\n",
      "[1, 1]\n"
     ]
    }
   ],
   "source": [
    "def min1(*args):\n",
    "    res = args[0]\n",
    "    for arg in args[1:]:\n",
    "        if arg < res:\n",
    "            res = arg\n",
    "    return res\n",
    "\n",
    "def min2(first, *rest):\n",
    "    for arg in rest:\n",
    "        if arg < first:\n",
    "            first = arg\n",
    "    return first\n",
    "\n",
    "def min3(*args):\n",
    "    tmp = list(args)\n",
    "    tmp.sort(  )\n",
    "    return tmp[0]\n",
    "\n",
    "print(min1(3,4,1,2))\n",
    "print(min2(\"bb\", \"aa\"))\n",
    "print(min3([2,2], [1,1], [3,3]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Funções como objetos de primeira classe\n",
    "# Funções anonimous\n",
    "# Funções class\n",
    "# Funções de ordem superior\n",
    "\n",
    "# Falta implementar\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
