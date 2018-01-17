using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace LogoDetector.Models
{
    public class DetectRequest
    {
        public string VidUrl { get; set; }
        public string[] TemplateUrls { get; set; }
    }
}