### nginx ingress 설치
~~~
kubectl create namespace ingress-nginx
kubectl apply -f ingress-nginx-deploy.yaml -n ingress-nginx
~~~

### ArgoCd 설치
~~~
kubectl create namespace argocd
kubectl apply -f argocd-install.yaml -n argocd
~~~

### kustomize 확인
~~~
kubectl kustomize manifests/overlays/prod
~~~