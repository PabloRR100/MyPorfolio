# Extract Arguments (room for adding here more dynamic arguments )
for i in "$@"
do
case $i in
    -p=*|--port=*)
    PORT="${i#*=}"
    shift # past argument=value
    ;;
    -d=*|--dir=*)
    DIR="${i#*=}"
    shift # past argument=value
esac
done

# Launch Jupyter in the Background
echo "[INFO]: Launching Jupyter Lab"
echo "[INFO]: Forward the corresponding port and access your jupyter project at http://localhost:${PORT}/"
jupyter lab \
  --NotebookApp.token="" \
  --ip="0.0.0.0" \
  --port="${PORT}" \
  --no-browser \
  --allow-root \
  --notebook-dir="${DIR}"
