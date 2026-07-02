## Cluster Label

The hub cluster Prometheus instance was configured with an external label:

```yaml
prometheus:
  prometheusSpec:
    externalLabels:
      cluster: hub
