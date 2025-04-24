namespace ClassroomAPI.Models
{
    public class Recommendation
    {
        public Guid RecommendationId { get; set; } = Guid.NewGuid();
        public string UserId { get; set; } = string.Empty;  // For whom recommendation is made
        public ApplicationUser? User { get; set; }

        public Guid MaterialId { get; set; }
        public Material? Material { get; set; }

        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
    }
}
