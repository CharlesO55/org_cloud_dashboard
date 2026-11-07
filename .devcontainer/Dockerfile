FROM mcr.microsoft.com/devcontainers/python:3.14-trixie

# Install system dependencies required by Google Antigravity
RUN rm -f /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
        wget \
        git \
        iproute2 \
        netbase \
        libatomic1 \
    && mkdir -p -m 755 /etc/apt/keyrings \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update \
    && apt-get install -y --no-install-recommends gh \
    && rm -rf /var/lib/apt/lists/*
    
# Install Google Cloud SDK system-wide and configure environment & shell completion
ENV PATH="/usr/local/gcloud/google-cloud-sdk/bin:${PATH}"
RUN curl -fsSL https://sdk.cloud.google.com | bash -s -- --disable-prompts --install-dir=/usr/local/gcloud \
    && ln -s /usr/local/gcloud/google-cloud-sdk/bin/* /usr/local/bin/ || true \
    && rm -f /usr/local/bin/bootstrapping \
    && echo 'source /usr/local/gcloud/google-cloud-sdk/path.bash.inc' >> /etc/bash.bashrc \
    && echo 'source /usr/local/gcloud/google-cloud-sdk/completion.bash.inc' >> /etc/bash.bashrc \
    && mkdir -p /etc/zsh \
    && echo 'source /usr/local/gcloud/google-cloud-sdk/path.zsh.inc' >> /etc/zsh/zshrc \
    && echo 'source /usr/local/gcloud/google-cloud-sdk/completion.zsh.inc' >> /etc/zsh/zshrc \
    && echo 'export PATH="/usr/local/gcloud/google-cloud-sdk/bin:${PATH}"' > /etc/profile.d/gcloud.sh