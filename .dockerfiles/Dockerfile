FROM        eb_ubuntu
MAINTAINER  dev@azelf.com

# 현재경로의 모든 파일들을 컨테이너의 /srv/deploy_eb_docker폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb_docker와 같은 효과
WORKDIR     /srv/deploy_eb_docker
# requirements설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/debug.txt

EXPOSE      80 8000

# 실행시
# docker run --rm -it -p 9000:8000 eb /bin/zsh