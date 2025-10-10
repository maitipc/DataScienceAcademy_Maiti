## ⚙️ Otimizações de Desempenho na Stack PySpark + Kafka

💡 Este guia resume boas práticas para otimizar **processamento e transmissão de dados** em pipelines que utilizam **PySpark** e **Kafka**, garantindo eficiência, escalabilidade e desempenho.

---

## 🧩 Kafka

### 🔧 Ajuste do tamanho dos batches
Configure o parâmetro `batch.size` conforme o volume de dados e recursos disponíveis.  
➡️ Equilibra **latência** e **throughput**.

### ⚖️ Particionamento eficiente
Garanta que os **tópicos** sejam bem particionados para distribuir a carga entre consumidores.

### 🗃️ Retenção de mensagens
Defina `retention.ms` ou `retention.bytes` de acordo com as necessidades do pipeline.  
➡️ Evita **sobrecarga desnecessária** no cluster.

### 🚦 Ajuste do `fetch.max.bytes`
Evite sobrecarregar o consumidor, especialmente em pipelines de **alta latência**.

---

## 🔥 PySpark

### 💾 Persistência adequada
Use `cache()` ou `persist()` **somente quando necessário**, evitando armazenar RDDs/Datasets desnecessariamente.

### ⚙️ Gerenciamento de particionamento
Ajuste o número de partições em RDDs ou DataFrames para equilibrar uso de recursos.  
Exemplo:

```python
df = df.repartition(8)      # redistribui os dados entre 8 partições
# ou
df = df.coalesce(4)         # reduz para 4 partições de forma otimizada
```

### 🚫 Evite ações desnecessárias
Minimize operações como count(), collect() e show() — elas forçam a execução prematura do pipeline.

### 🧠 Use APIs estruturadas
Prefira DataFrames ou Datasets em vez de RDDs — o Catalyst Optimizer faz ajustes automáticos para melhor performance.

---

## Integração PySpark ↔️ Kafka

### ⏱️ Batch Size e Frequência
No Structured Streaming, ajuste:

`maxOffsetsPerTrigger`
`trigger`

Esses parâmetros controlam o volume de dados por microbatch, evitando gargalos.

```python
stream = spark.readStream \
  .format("kafka") \
  .option("maxOffsetsPerTrigger", 5000) \
  .load()
```

### 💾 Checkpointing
Defina um diretório de checkpoint para permitir recuperação em caso de falhas:

```python
query.writeStream \
  .option("checkpointLocation", "/path/to/checkpoint") \
  .start()
```

### 🎯 Offset Management
Use `startingOffsets` e `endingOffsets` estrategicamente para evitar sobrecarga inicial ou reprocessamento desnecessário.

---

## ⚙️ Geral

### 📊 Monitoramento

Ferramentas úteis:
`Kafka Manager`
`Spark UI`
`Confluent Control Center`

🔍 Acompanhe gargalos e métricas em tempo real.

### 💡 Recursos alocados
Ajuste:
```bash
--executor-memory
--executor-cores
--num-executors
```
para balancear carga e performance.

### 📦 Compactação
Ative compressão de mensagens no Kafka (snappy, lz4, etc.)

➡️ Reduz largura de banda e uso de armazenamento.

---

## ✅ Conclusão

Combinar essas práticas melhora:

⚡ Desempenho e latência

📈 Escalabilidade

🧠 Uso eficiente de recursos

Um pipeline bem ajustado entre PySpark + Kafka garante alta performance e estabilidade em ambientes de dados em tempo real.
