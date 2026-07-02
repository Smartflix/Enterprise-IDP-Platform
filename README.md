# Enterprise Internal Developer Platform (IDP)

A production-inspired, multi-cluster Internal Developer Platform built with Kubernetes, ArgoCD, GitOps, Prometheus, Grafana, Loki, Helm, GitHub Actions, and Platform Engineering best practices.

## Milestone 1 – Building a Multi-Cluster GitOps Foundation

### Overview

The goal of this project is to build an Enterprise Internal Developer Platform (IDP) that simplifies how applications are deployed, managed, and monitored across multiple Kubernetes clusters. Rather than deploying applications manually, I wanted to create a platform where Git becomes the single source of truth and deployments happen automatically using GitOps.

For the first milestone, I focused on building the platform's foundation by creating a hub-and-spoke architecture with two Kubernetes clusters managed through Argo CD.

---

# What I Built

During this milestone, I created a local enterprise-style Kubernetes environment using Kind.

The environment consists of:

* A **Hub Cluster**, which hosts Argo CD and acts as the central management cluster.
* A **Development Cluster**, where applications are deployed.
* A local Docker Registry used to store container images.
* An NGINX Ingress Controller to expose applications.
* Helm charts to package and deploy applications consistently.

The first application deployed on the platform is the **Payments API**, which is fully managed through Argo CD.

---

# Architecture

```text
                       GitHub Repository
                               │
                               ▼
                          Argo CD (Hub)
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
         Hub Cluster                     Dev Cluster
       (Management)                  (Application)
                                               │
                                               ▼
                                           Helm Chart
                                               │
                                               ▼
                                          Payments API
                                               │
                                    Kubernetes Service
                                               │
                                               ▼
                                       NGINX Ingress
                                               │
                                               ▼
                               /health → {"status":"ok"}
```

---

# What Was Accomplished

By the end of this milestone, the platform was able to:

* Manage multiple Kubernetes clusters from a single Argo CD instance.
* Automatically deploy applications from a GitHub repository.
* Deploy applications using Helm charts.
* Route external traffic through an Ingress Controller.
* Serve application health checks successfully.
* Maintain a healthy GitOps workflow where Kubernetes always matches the desired state stored in Git.

---

# Challenges Along the Way

Building the platform wasn't just about installing tools. Several real-world issues had to be diagnosed and resolved.

### ImagePullBackOff

One of the biggest challenges was getting Kubernetes to pull the Payments API image from the local Docker registry.

The deployment repeatedly failed because the image was either unavailable or not accessible from inside the Kind cluster.

To resolve this, I:

* Verified the Docker registry configuration.
* Connected the registry to the Kind network.
* Confirmed the image existed in the registry.
* Loaded the image into the cluster.
* Restarted the deployment and validated the rollout.

This troubleshooting process reinforced the importance of understanding how Kubernetes interacts with local registries in development environments.

---

### Argo CD Connectivity

During testing, the Argo CD CLI stopped communicating with the server because the port-forward session had ended.

The issue was resolved by re-establishing the port-forward connection and reconnecting the CLI.

Although simple, it highlighted an important aspect of working with local Kubernetes environments—many services rely on temporary port-forward sessions during development.

---

### Ingress Configuration

Initially, the application was healthy but inaccessible through the expected URL.

After validating the Deployment, Service, and application health independently, the issue was traced to the local Ingress access method.

Once the Ingress Controller was correctly port-forwarded, the application became available through its configured hostname.

---

# Final Validation

At the end of the milestone, the Payments API was fully operational.

The application responded successfully to its health endpoint:

```json
{
  "status": "ok"
}
```

Argo CD reported the application as:

* **Synced**
* **Healthy**

The Kubernetes Deployment completed successfully, and the application was accessible through the configured Ingress.

---

# Skills Demonstrated

This milestone provided practical experience with:

* Kubernetes cluster administration
* Multi-cluster architecture
* GitOps workflows
* Argo CD
* Helm packaging
* Docker Registry management
* Kubernetes networking
* NGINX Ingress
* Service discovery
* Troubleshooting Kubernetes deployments
* Application lifecycle management

---

# Key Outcomes

By completing this milestone, I now have a working GitOps platform capable of managing multiple Kubernetes clusters from a central control plane.

Applications can be deployed through Git, automatically synchronized by Argo CD, and exposed through Kubernetes networking components.

This provides a strong foundation for expanding the platform into a more production-like environment.

---

# Next Steps

With the core platform now operational, the next milestone will focus on improving observability across the environment.

The plan is to introduce:

* Prometheus for metrics collection
* Grafana dashboards
* Loki for centralized logging
* Promtail for log collection
* Multi-cluster monitoring
* Centralized operational visibility

These additions will transform the platform from a deployment solution into a fully observable Internal Developer Platform capable of supporting production-style operations.

Stage 1 marked complete
New architecture image
Screenshot of Argo CD
Screenshot of Payments API