using UnityEngine;

public class CameraController : MonoBehaviour
{
    [Header("Alvos e Sensibilidade")]
    public Transform target; 
    public float mouseSensitivity = 100f;
    
    [Header("Configurações de Distância (Offset)")]
    public Vector3 offset = new Vector3(0, 1.5f, -3f); // O valor de Z será controlado pelo zoom

    [Header("Configurações de Zoom")]
    public float zoomSpeed = 2f;
    public float minZoomDist = -0.5f;  // Mais perto da Elowen
    public float maxZoomDist = -8f; // Mais longe da Elowen
    public float zoomSmoothness = 10f;

    private float rotationX = 0f;
    private float rotationY = 0f;
    private float currentZ; // Para suavizar o movimento de zoom

    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked;
        currentZ = offset.z; // Inicializa com a distância atual
    }

    void LateUpdate()
    {
        if (target == null) return;

        // --- LÓGICA DE ROTAÇÃO ---
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity * Time.deltaTime;

        rotationY += mouseX;
        rotationX += mouseY;
        rotationX = Mathf.Clamp(rotationX, -40f, 85f);

        // --- LÓGICA DE ZOOM ---
        float scroll = Input.GetAxis("Mouse ScrollWheel");
        if (scroll != 0)
        {
            // O scroll aumenta ou diminui o valor de Z
            currentZ += scroll * zoomSpeed * 1f;
            // Limita o zoom (lembrando que os valores são negativos porque a câmera fica "atrás")
            currentZ = Mathf.Clamp(currentZ, maxZoomDist, minZoomDist);
        }

        // Suaviza a transição do zoom (opcional, mas fica mais profissional)
        offset.z = Mathf.Lerp(offset.z, currentZ, Time.deltaTime * zoomSmoothness);

        // --- APLICAÇÃO FINAL ---
        Quaternion rotation = Quaternion.Euler(rotationX, rotationY, 0);
        
        // Multiplicamos a rotação pelo offset para orbitar o alvo
        transform.position = target.position + rotation * offset;

        // Olha para o alvo (ajustado para o tronco/cabeça)
        transform.LookAt(target.position + Vector3.up * 1.5f);
    }
}