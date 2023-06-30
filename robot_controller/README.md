# Guia de Instalação do Pacote `safemc` no ROS 2

Siga as etapas abaixo para instalar e executar o pacote `safemc` no ROS 2:

1. Certifique-se de ter o ROS 2 instalado em seu sistema. Caso não tenha, você pode seguir as instruções de instalação fornecidas pela documentação oficial do ROS 2.

2. Abra um terminal e execute o seguinte comando para compilar o pacote `safemc`:

   ```shell
   colcon build --packages-select safemc
   ```

   Esse comando irá compilar apenas o pacote `safemc` em vez de compilar todos os pacotes do projeto.

3. Após a conclusão da compilação, execute o seguinte comando para configurar o ambiente de trabalho do ROS 2:

   ```shell
   source install/setup.bash
   ```

   Isso carregará as variáveis de ambiente necessárias e configurará o ambiente de trabalho para o pacote `safemc`.

4. Instale o pacote `rosbridge_server` executando o seguinte comando:

   ```shell
   sudo apt-get install ros-<rosdistro>-rosbridge-server
   ```

   Certifique-se de substituir `<rosdistro>` pelo nome correto da distribuição ROS que você está utilizando.

5. Configure o ambiente de trabalho do ROS 2 executando o seguinte comando:

   ```shell
   source /opt/ros/<rosdistro>/setup.bash
   ```

   Certifique-se de substituir `<rosdistro>` pelo nome correto da distribuição ROS que você está utilizando.

6. Inicie o servidor do `rosbridge` executando o seguinte comando:

   ```shell
   ros2 launch rosbridge_server rosbridge_websocket_launch.xml
   ```

7. Após a conclusão dessas etapas, execute o pacote `safemc` usando o seguinte comando:

   ```shell
   ros2 run safemc go2goal
   ```

   Esse comando iniciará a execução do pacote `safemc` e ativará o nó `go2goal` para realizar suas funcionalidades.

Parabéns! Agora você instalou com sucesso o pacote `safemc` no ROS 2 e está pronto para utilizar o nó `go2goal`. Certifique-se de que todos os pré-requisitos do pacote estejam atendidos antes de executá-lo.

Espero que este guia seja útil para você. Se você tiver alguma dúvida adicional, não hesite em perguntar.

```

Certifique-se de substituir `<rosdistro>` pelo nome correto da distribuição ROS que você está utilizando, como "foxy" ou "galactic".
```
