USE [CSUTest]
GO
/****** Object:  Table [dbo].[Invoice_Details]    Script Date: 24.12.2020 17:41:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Invoice_Details](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Sales_Id] [bigint] NULL,
	[Id_Product] [bigint] NULL,
	[Price] [smallmoney] NULL,
	[Amount] [int] NULL,
	[Total] [real] NULL,
 CONSTRAINT [PK_Invoice_Details] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Invoice_Main]    Script Date: 24.12.2020 17:41:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Invoice_Main](
	[Sales_Id] [bigint] IDENTITY(1,1) NOT NULL,
	[PaymentWay] [int] NULL,
	[ClientName] [nvarchar](50) NULL,
	[TotalCost] [real] NULL,
	[InDate] [datetime2](7) NULL,
 CONSTRAINT [PK_Invoice_Main_1] PRIMARY KEY CLUSTERED 
(
	[Sales_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Products]    Script Date: 24.12.2020 17:41:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Products](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[ProductName] [nvarchar](50) NULL,
	[ProductType] [int] NULL,
	[Price] [smallmoney] NULL,
	[Color] [int] NULL,
	[size] [nchar](10) NULL,
	[TradeMark] [nvarchar](50) NULL,
	[Amount] [int] NULL,
 CONSTRAINT [PK_Products] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Invoice_Main] ADD  CONSTRAINT [DF_Invoice_Main_InDate]  DEFAULT (getdate()) FOR [InDate]
GO
